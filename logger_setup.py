import logging
from logging.handlers import TimedRotatingFileHandler
from rich.logging import RichHandler

def setup_logger():
    logger = logging.getLogger("CleanDeskLogger")
    logger.setLevel(logging.DEBUG)

    # Console handler com Rich para logs coloridos
    console_handler = RichHandler()
    console_handler.setLevel(logging.DEBUG)

    # Handler para arquivo com rotação diária
    file_handler = TimedRotatingFileHandler("logs/clean_desk.log", when="midnight", backupCount=7)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()
