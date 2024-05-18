import logging

def add_query_logging():
    logger_db_client = logging.getLogger("tortoise.db_client")
    logger_db_client.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    logger_db_client.addHandler(sh)
