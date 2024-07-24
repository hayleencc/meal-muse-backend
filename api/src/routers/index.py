from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index() -> dict:
    return {"Meal Muse": "0.1"}
