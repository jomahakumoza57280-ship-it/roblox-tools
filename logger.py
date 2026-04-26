import logging
import os
from logging.handlers import RotatingFileHandler

# Configure logger with rotation

def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    # Create a logger
    logger = logging.getLogger('roblox_tools')
    logger.setLevel(logging.DEBUG)

    # Create a file handler for logging
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter for logging output
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger has been set up!')
