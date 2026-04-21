import re

class InputValidator:
    @staticmethod
    def validate_username(username):
        if not isinstance(username, str):
            raise ValueError('Username must be a string.')
        if not 3 <= len(username) <= 20:
            raise ValueError('Username must be between 3 and 20 characters long.')
        if not re.match('^[a-zA-Z0-9_]+$', username):
            raise ValueError('Username can only contain alphanumeric characters and underscores.')

    @staticmethod
    def validate_password(password):
        if not isinstance(password, str):
            raise ValueError('Password must be a string.')
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        if not re.search('[A-Z]', password):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not re.search('[0-9]', password):
            raise ValueError('Password must contain at least one number.')

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise ValueError('Email must be a string.')
        email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if not re.match(email_regex, email):
            raise ValueError('Invalid email format.')
