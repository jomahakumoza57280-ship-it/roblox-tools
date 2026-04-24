from typing import Any, Dict, Optional


def validate_class_id(class_id: int) -> bool:
    """
    Validates if the given class ID is a positive integer.

    Args:
        class_id (int): The class ID to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return class_id > 0


def validate_user_data(user_data: Dict[str, Any]) -> Optional[str]:
    """
    Validates user data against expected fields.

    Args:
        user_data (Dict[str, Any]): A dictionary containing user data.

    Returns:
        Optional[str]: Returns a validation error message if invalid, otherwise None.
    """
    required_fields = ['username', 'age', 'email']
    for field in required_fields:
        if field not in user_data:
            return f'Missing required field: {field}'
    if not isinstance(user_data['age'], int) or user_data['age'] <= 0:
        return 'Age must be a positive integer.'
    if not isinstance(user_data['username'], str) or len(user_data['username']) < 3:
        return 'Username must be at least 3 characters long.'
    return None


def validate_item_id(item_id: int) -> bool:
    """
    Validates if the given item ID is a positive integer.

    Args:
        item_id (int): The item ID to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return item_id > 0
