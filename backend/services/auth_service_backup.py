from backend.utils.security import (
    hash_password,
    verify_password
)

from backend.utils.jwt_handler import (
    create_access_token
)


# Temporary storage
fake_users_db = {}


def register_user(username: str, email: str, password: str):
    """
    Register a new user
    """

    if email in fake_users_db:
        return None

    hashed_password = hash_password(password)

    fake_users_db[email] = {
        "username": username,
        "email": email,
        "password": hashed_password
    }

    return {
        "username": username,
        "email": email
    }


def login_user(email: str, password: str):
    """
    Login user and return JWT token
    """

    user = fake_users_db.get(email)

    if not user:
        return None

    if not verify_password(
        password,
        user["password"]
    ):
        return None

    token = create_access_token({
        "sub": user["email"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

-- Table: users

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);