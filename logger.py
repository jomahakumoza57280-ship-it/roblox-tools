import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_size=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  

    # Create a directory for logs if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a rotating file handler
    handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_size, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

logger = setup_logger()  # Instantiate the logger
logger.info('Logger is set up and ready!')