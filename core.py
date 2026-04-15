import time
import functools


def performance_timer(func):
    """Decorator to measure execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {{execution_time}} seconds")
        return result
    return wrapper

@performance_timer
def heavy_computation(data):
    """Simulate a heavy computation task."""
    total = 0
    for num in range(data):
        total += num ** 2
    return total

@performance_timer
def process_data(data):
    """Process the input data with optimizations."""
    processed = [heavy_computation(item) for item in data]
    return processed

if __name__ == '__main__':
    sample_data = range(10000)
    results = process_data(sample_data)
    print(results)
