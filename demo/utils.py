import hashlib


def hash_password(password: str) -> str:
    """
    Generate SHA-256 hash of a password.
    """
    return hashlib.sha256(password.encode()).hexdigest()
