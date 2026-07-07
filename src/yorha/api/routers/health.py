from fastapi import APIRouter

from yorha.kernel.runtime import runtime

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {
        "status": "ok",
        **runtime.info(),
    }