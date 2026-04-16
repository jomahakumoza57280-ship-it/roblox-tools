import time

class RobloxPerformance:
    def __init__(self):
        self.logs = []

    def log_execution_time(self, func):
        """
        Decorator to log execution time of functions.
        """
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            self.logs.append({
                'function': func.__name__,
                'execution_time': execution_time
            })
            return result
        return wrapper

    def get_logs(self):
        """
        Returns the collected execution time logs.
        """
        return self.logs

    @log_execution_time
    def expensive_operation(self, iterations):
        """
        Simulates a time-consuming operation.
        """
        total = 0
        for i in range(iterations):
            total += i * 2
        return total

# Example usage
if __name__ == '__main__':
    performance = RobloxPerformance()
    performance.expensive_operation(10000)
    print(performance.get_logs())