import os
import uuid

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.ocr_service import extract_text_from_image

from services.chroma_service import add_document

from services.llm_service import (
    classify_document,
    extract_entities,
    generate_summary
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/extract")
async def extract_document(
    file: UploadFile = File(...)
):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    filepath = os.path.join(
        UPLOAD_DIR,
        filename
    )

    with open(filepath, "wb") as buffer:
        buffer.write(
            file.file.read()
        )

    text = extract_text_from_image(
        filepath
    )

    add_document(
        text=text,
        doc_id=filename
    )

    document_type = classify_document(
        text
    )

    structured_data = extract_entities(
        text
    )

    summary = generate_summary(
        text
    )

    return {
        "filename": filename,
        "document_type": document_type,
        "ocr_text": text,
        "structured_data": structured_data,
        "summary": summary
    }