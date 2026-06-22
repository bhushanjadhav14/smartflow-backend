from fastapi import APIRouter
from backend.services.target_service import get_target_count

router = APIRouter()


@router.get("/target-count")
def target_count():
    return get_target_count()