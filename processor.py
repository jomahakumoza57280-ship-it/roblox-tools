from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Processes a list of data dictionaries.
    
    Args:
        data (List[Dict[str, Any]]): A list of dictionaries,
        where each dictionary contains data to be processed.
    
    Returns:
        List[Dict[str, Any]]: A list of processed data dictionaries.
    """
    processed_data = []
    for item in data:
        processed_item = {
            'id': item['id'],
            'name': item['name'].strip(),
            'value': item['value'] if item['value'] > 0 else 0
        }
        processed_data.append(processed_item)
    return processed_data


def display_data(data: List[Dict[str, Any]]) -> None:
    """
    Displays the processed data in a readable format.
    
    Args:
        data (List[Dict[str, Any]]): A list of processed data dictionaries.
    """
    for item in data:
        print(f"ID: {item['id']}, Name: {item['name']}, Value: {item['value']}")