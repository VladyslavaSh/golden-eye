import requests

from models import XRate, peewee_datetime
from config import logging, LOGGER_CONFIG


log = logging.getLogger("PrivatApi")
handler = logging.FileHandler(LOGGER_CONFIG["file"])
handler.setLevel(LOGGER_CONFIG["level"])
handler.setFormatter(LOGGER_CONFIG["formatter"])
log.addHandler(handler)
log.setLevel(LOGGER_CONFIG["level"])


def update_xrates(from_currency, to_currency):
    log.info("Started update for: %s=>%s" % (from_currency, to_currency))
    # get the rate from the DB
    xrate = XRate.select().where(XRate.from_currency == from_currency,
                                 XRate.to_currency == to_currency).first()

    log.debug("rate before: %s", xrate)
    # get a new value of the rate from the Privat and save it in the xrate object
    xrate.rate = get_privat_rate(from_currency)
    # update field updated
    xrate.updated = peewee_datetime.datetime.now()
    xrate.save()

    log.debug("rate after: %s", xrate)
    log.info("Finished update for: %s=>%s" % (from_currency, to_currency))


def get_privat_rate(from_currency):
    response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    response_json = response.json()
    log.debug("Privat response: %s" % response_json)
    usd_rate = find_usd_rate(response_json)

    return usd_rate


def find_usd_rate(response_data):
    for e in response_data:
        if e["ccy"] == "USD":
            return float(e["sale"])

    raise ValueError("Invalid Privat response: USD not found")
