import time

class PerformanceOptimizer:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        start_time = time.time()
        results = []
        # Use set for faster lookups
        data_set = set(self.data)
        for item in data_set:
            processed_item = self._heavy_computation(item)
            results.append(processed_item)
        end_time = time.time()
        print(f"Processing time: {end_time - start_time} seconds")
        return results

    def _heavy_computation(self, item):
        # Simulate a heavy computation
        time.sleep(0.01)  # Simulate delay
        return item * 2  # Just an example operation

if __name__ == '__main__':
    optimizer = PerformanceOptimizer(range(100))
    results = optimizer.process_data()
    print(results)