import logging
from config import LOG_LEVEL

def setup_logger():
    logger = logging.getLogger("gossip")
    logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
    handler = logging.FileHandler("gossip.log", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()
