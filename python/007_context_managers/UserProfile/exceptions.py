class ValidationError(Exception):
    """ValidationError base exception."""


class FullNameError(ValidationError):
    """Ivalid full name exception."""


class EmailError(ValidationError):
    """Invalid email exception."""


class PasswordError(ValidationError):
    """Invalid password."""


class PhoneError(ValidationError):
    """Invalid phone."""
