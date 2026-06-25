from fastapi import Header, HTTPException

from backend.utils.jwt_handler import verify_token


def get_current_user(
    authorization: str = Header(None)
):
    """
    Verify JWT token from Authorization header
    """

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    try:
        token = authorization.replace(
            "Bearer ",
            ""
        )

        payload = verify_token(token)

        return payload

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )