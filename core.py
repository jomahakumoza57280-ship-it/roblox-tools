import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_function(self, func):
        """Decorator to time a function's execution."""
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def average_time(self):
        """Returns the average execution time of tracked functions."""
        return sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0

    def clear_times(self):
        """Clears the recorded execution times."""
        self.execution_times.clear()

# Example of usage
if __name__ == '__main__':
    optimizer = PerformanceOptimizer()

    @optimizer.time_function
    def example_function(delay):
        time.sleep(delay)

    # Test the performance measurement
    for i in range(5):
        example_function(i * 0.1)

    print(f'Average execution time: {optimizer.average_time()} seconds')