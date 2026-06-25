from sqlalchemy import text

from backend.database.db import engine

from backend.utils.security import (
    hash_password,
    verify_password
)

from backend.utils.jwt_handler import (
    create_access_token
)


def register_user(username: str, email: str, password: str):

    with engine.connect() as conn:

        existing_user = conn.execute(
            text("""
                SELECT email
                FROM users
                WHERE email = :email
            """),
            {"email": email}
        ).fetchone()

        if existing_user:
            return None

        hashed_password = hash_password(password)

        conn.execute(
            text("""
                INSERT INTO users
                (username, email, password)
                VALUES
                (:username, :email, :password)
            """),
            {
                "username": username,
                "email": email,
                "password": hashed_password
            }
        )

        conn.commit()

    return {
        "username": username,
        "email": email
    }


def login_user(email: str, password: str):

    with engine.connect() as conn:

        user = conn.execute(
            text("""
                SELECT username,
                       email,
                       password
                FROM users
                WHERE email = :email
            """),
            {"email": email}
        ).fetchone()

    if not user:
        return None

    if not verify_password(
        password,
        user[2]
    ):
        return None

    token = create_access_token({
        "sub": user[1]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }