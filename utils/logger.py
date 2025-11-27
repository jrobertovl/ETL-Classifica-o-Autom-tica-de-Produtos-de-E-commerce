import logging

def get_logger():
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    return logging.getLogger("ETL")
