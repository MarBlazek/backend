from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_exhibits():
    return [{"id": 1, "name": "Ruke", "artist": "Marinela"}]