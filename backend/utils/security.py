from passlib.context import CryptContext


# Use bcrypt algorithm for password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    """
    Convert plain password into secure hash
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    """
    Verify login password with stored hash
    """
    return pwd_context.verify(
        plain_password,
        hashed_password
    )