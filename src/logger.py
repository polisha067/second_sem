import logging

logging.basicConfig(
    filename="polisha.log",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s"
)

log = logging.getLogger('polisha')

def log_error(text):
    log.error(text)