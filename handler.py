import json

class CustomError(Exception):
    pass

def handle_request(data):
    if not isinstance(data, dict):
        raise CustomError("Invalid data type, expected a dictionary.")
    if 'action' not in data:
        raise CustomError("Missing 'action' key in data.")
    if data['action'] not in ['create', 'update', 'delete']:
        raise CustomError("Invalid action specified.")
    
    try:
        result = process_action(data)
    except Exception as e:
        raise CustomError(f"An error occurred while processing the action: {str(e)}")
    return result


def process_action(data):
    action = data['action']
    # Simulate processing logic
    if action == 'create':
        return json.dumps({'status': 'success', 'message': 'Created successfully.'})
    elif action == 'update':
        return json.dumps({'status': 'success', 'message': 'Updated successfully.'})
    elif action == 'delete':
        return json.dumps({'status': 'success', 'message': 'Deleted successfully.'})

if __name__ == '__main__':
    test_data = {'action': 'create'}
    try:
        response = handle_request(test_data)
        print(response)
    except CustomError as e:
        print(f'Error: {str(e)}')