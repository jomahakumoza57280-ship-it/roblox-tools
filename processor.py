import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RobloxDataProcessor:
    def __init__(self, data):
        self.data = data

    def validate_data(self):
        if not isinstance(self.data, list):
            logger.error('Data is not a list')
            raise ValueError('Expected a list, got {}'.format(type(self.data).__name__))
        if len(self.data) == 0:
            logger.error('Data list is empty')
            raise ValueError('Data list cannot be empty')

    def process_data(self):
        self.validate_data()
        processed = []
        for item in self.data:
            if not isinstance(item, dict):
                logger.warning('Skipping non-dict item: {}'.format(item))
                continue
            processed_data = self.process_item(item)
            if processed_data:
                processed.append(processed_data)
        return processed

    def process_item(self, item):
        try:
            # Example processing logic
            return {'id': item['id'], 'name': item.get('name', 'Unknown')}
        except KeyError as e:
            logger.error('Missing key in item: {}'.format(e))
            return None
        except Exception as e:
            logger.error('Error processing item: {}'.format(e))
            return None

if __name__ == '__main__':
    sample_data = [{'id': 1, 'name': 'Item1'}, {'id': 2}, 'Invalid item']
    processor = RobloxDataProcessor(sample_data)
    try:
        result = processor.process_data()
        print(json.dumps(result, indent=2))
    except ValueError as e:
        logger.error('Data processing failed: {}'.format(e))