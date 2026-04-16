class RobloxError(Exception):
    """Base class for all Roblox-related exceptions."""
    pass

class InvalidAssetIDError(RobloxError):
    """Raised when an invalid asset ID is used."""
    def __init__(self, asset_id, message="Invalid Asset ID provided."):
        self.asset_id = asset_id
        self.message = message
        super().__init__(self.message)

class ConnectionError(RobloxError):
    """Raised for connection issues with Roblox API."""
    def __init__(self, message="Failed to connect to the Roblox server."):
        self.message = message
        super().__init__(self.message)

class RateLimitExceededError(RobloxError):
    """Raised when API rate limit is exceeded."""
    def __init__(self, limit, message="Rate limit exceeded."):
        self.limit = limit
        self.message = message
        super().__init__(self.message)

class PermissionDeniedError(RobloxError):
    """Raised when permission is denied for an action."""
    def __init__(self, action, message="Permission denied for this action."):
        self.action = action
        self.message = message
        super().__init__(self.message)