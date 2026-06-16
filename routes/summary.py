from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
def summary():

    return {
        "status": "ready"
    }