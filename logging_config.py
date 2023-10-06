import logging


def setup_logging():
    logging.basicConfig(level=logging.ERROR,
                        format='[%(asctime)s] %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger()

    file_handler = logging.FileHandler('my_log.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.ERROR)
    console_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    logger.addHandler(console_handler)

    return logger
