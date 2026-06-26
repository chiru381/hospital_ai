import os

from app.services.document.pdf_service import read_pdf
from app.services.document.word_service import read_docx
from app.services.document.excel_service import read_excel
from app.services.document.csv_service import read_csv
from app.services.document.ppt_service import read_ppt
from app.services.document.text_service import read_txt
from app.services.document.json_service import read_json


SUPPORTED_FILES = {
    ".pdf": read_pdf,
    ".docx": read_docx,
    ".xlsx": read_excel,
    ".csv": read_csv,
    ".pptx": read_ppt,
    ".txt": read_txt,
    ".json": read_json,
}


def load_document(file_path: str):

    ext = os.path.splitext(file_path)[1].lower()

    if ext not in SUPPORTED_FILES:
        raise Exception(f"{ext} file is not supported.")

    return SUPPORTED_FILES[ext](file_path)