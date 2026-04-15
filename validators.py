import re

class ValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError('Username must be a string.')
    if len(username) < 3:
        raise ValidationError('Username must be at least 3 characters long.')
    if len(username) > 20:
        raise ValidationError('Username must not exceed 20 characters.')
    if not re.match('^[a-zA-Z0-9_]+$', username):
        raise ValidationError('Username can only contain letters, numbers, and underscores.')
    return True

def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError('Email must be a string.')
    if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValidationError('Invalid email format.')
    return True

def validate_password(password):
    if not isinstance(password, str):
        raise ValidationError('Password must be a string.')
    if len(password) < 6:
        raise ValidationError('Password must be at least 6 characters long.')
    if not re.search('[A-Za-z]', password) or not re.search('[0-9]', password):
        raise ValidationError('Password must contain both letters and numbers.')
    return True
