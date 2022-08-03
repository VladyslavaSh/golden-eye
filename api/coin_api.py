from api import _Api


class Api(_Api):

    def __init__(self):
        super().__init__("CryptonatorApi")

    def _update_rate(self, xrate):
        rate = self._get_api_rate(xrate.from_currency, xrate.to_currency)
        return rate

    def _get_api_rate(self, from_currency, to_currency):
        aliases_map = {1000: "BTC", 980: "UAH", 978: "EUR", 840: "USD"}

        if from_currency not in aliases_map:
            raise ValueError(f"Invalid from_currency: {from_currency}")

        if to_currency not in aliases_map:
            raise ValueError(f"Invalid to_currency: {to_currency}")

        # https://rest.coinapi.io/v1/exchangerate/BTC/UAH
        # url_end depends on the currency
        url_end = f"{aliases_map[from_currency]}/{aliases_map[to_currency]}"
        url = f"https://rest.coinapi.io/v1/exchangerate/{url_end}"
        headers = {'X-CoinAPI-Key': '287DDFAB-AF99-4D1D-A7AF-4ABE7C5A0E02'}
        response = self._send_request(url=url, method="get", headers=headers)
        response_json = response.json()
        self.log.debug("CoinAPI response: %s" % response_json)
        rate = self._find_rate(response_json)

        return rate

    # parsing + return the exchange rate
    def _find_rate(self, response_data):
        if "rate" not in response_data:
            raise ValueError(f"Invalid CoinAPI response: rate not set")

        return float(response_data["rate"])
