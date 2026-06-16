import os
import uuid

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    with open(path, "wb") as buffer:
        buffer.write(
            file.file.read()
        )

    return {
        "path": path
    }