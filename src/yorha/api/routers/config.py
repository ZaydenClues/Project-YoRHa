from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/config")
async def config():
    return {
        "name": "YoRHa",
        "description": "YoRHa Tool Server",
        "version": "0.1.0"
    }