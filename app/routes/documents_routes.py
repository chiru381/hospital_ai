from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os

from app.services.document.document_loader import load_document

router = APIRouter(
    prefix="/document",
    tags=["Document"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/read")
async def read_document(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = load_document(file_path)

        return {
            "filename": file.filename,
            "content": text
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )