import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def set_level(self, level):
        self.logger.setLevel(level)

    def log_performance(self, func):
        import time
        
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.info(f'Performance: {func.__name__} took {elapsed_time:.4f}s')
            return result
        
        return wrapper
