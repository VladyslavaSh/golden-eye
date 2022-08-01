from api import _Api


class Api(_Api):
    def __init__(self):
        super().__init__("PrivatApi")

    def _update_rate(self, xrate):
        rate = self._get_monobank_rate(xrate.from_currency, xrate.to_currency)
        return rate

    def _get_monobank_rate(self, from_currency, to_currency):
        response = self._send_request(url="https://api.monobank.ua/bank/currency",
                                      method="get")
        response_json = response.json()
        self.log.debug("Monobank response: %s" % response_json)
        rate = self._find_rate(response_json, from_currency, to_currency)

        return rate

    def _find_rate(self, response_data, from_currency, to_currency):
        # monobank_aliases_map = {978: "EUR"}

        # if from_currency not in monobank_aliases_map:
        #    raise ValueError(f"Invalid from_currency: {from_currency}")

        # currency_alias = monobank_aliases_map[from_currency]

        for e in response_data:
            if e["currencyCodeA"] == from_currency and e["currencyCodeB"] == to_currency:
                return float(e["rateSell"])

        raise ValueError(f"Invalid Monobank response: {from_currency} not found")
