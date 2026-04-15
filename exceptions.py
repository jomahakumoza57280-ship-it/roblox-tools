class RobloxError(Exception):
    """Base class for all Roblox-related exceptions."""
    pass


class AssetNotFoundError(RobloxError):
    """Exception raised when an asset is not found."""
    def __init__(self, asset_id: int, message: str = "Asset not found.") -> None:
        super().__init__(message)
        self.asset_id = asset_id
        self.message = message

    def __str__(self) -> str:
        return f'{self.message} (Asset ID: {self.asset_id})'


class PermissionDeniedError(RobloxError):
    """Exception raised when permission is denied."""
    def __init__(self, action: str, message: str = "Permission denied.") -> None:
        super().__init__(message)
        self.action = action
        self.message = message

    def __str__(self) -> str:
        return f'{self.message} (Action: {self.action})'


class InvalidDataError(RobloxError):
    """Exception raised for invalid input data."""
    def __init__(self, data: str, message: str = "Invalid data provided.") -> None:
        super().__init__(message)
        self.data = data
        self.message = message

    def __str__(self) -> str:
        return f'{self.message} (Data: {self.data})'