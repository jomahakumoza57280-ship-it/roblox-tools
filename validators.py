import re

class RobloxValidator:
    @staticmethod
    def is_valid_username(username: str) -> bool:
        """
        Validate the username according to Roblox rules:
        - Must be 3-20 characters long
        - May only contain alphanumeric characters and underscores
        - Must not start or end with an underscore
        """
        if not (3 <= len(username) <= 20):
            return False
        if username.startswith('_') or username.endswith('_'):
            return False
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False
        return True

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate the email format using regular expressions.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_display_name(name: str) -> bool:
        """
        Validate the display name for Roblox:
        - Must be 1-21 characters long
        - Cannot contain special characters besides spaces and underscores
        """
        if not (1 <= len(name) <= 21):
            return False
        if not re.match(r'^[a-zA-Z0-9_ ]+$', name):
            return False
        return True
