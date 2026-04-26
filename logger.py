import logging


def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """
    Setup a logger with the specified name and log file.

    Args:
        name (str): The name of the logger.
        log_file (str): The log file path to write logs.
        level (int): The logging level (default is INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create file handler that logs to a file
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(fh)
    return logger


def log_info(logger: logging.Logger, message: str) -> None:
    """
    Log an information message.

    Args:
        logger (logging.Logger): The logger instance to use.
        message (str): The information message to log.
    """
    logger.info(message)


def log_error(logger: logging.Logger, message: str) -> None:
    """
    Log an error message.

    Args:
        logger (logging.Logger): The logger instance to use.
        message (str): The error message to log.
    """
    logger.error(message)