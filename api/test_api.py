from models import XRate, peewee_datetime

from config import logging, LOGGER_CONFIG

log = logging.getLogger("TestApi")
handler = logging.FileHandler(LOGGER_CONFIG["file"])
handler .setLevel(LOGGER_CONFIG["level"])
handler .setFormatter(LOGGER_CONFIG["formatter"])
log.addHandler(handler)
log.setLevel(LOGGER_CONFIG["level"])


def update_xrates(from_currency, to_currency):
    log.info("Started update for: %s=>%s" % (from_currency, to_currency))
    xrate = XRate.select().where(XRate.from_currency == from_currency,
                                 XRate.to_currency == to_currency).first()

    log.debug("rate before: %s", xrate)
    xrate.rate += 0.01
    xrate.updated = peewee_datetime.datetime.now()
    xrate.save()

    log.debug("rate after: %s", xrate)
    log.info("Finished update for: %s=>%s" % (from_currency, to_currency))
