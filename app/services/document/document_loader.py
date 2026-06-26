import os

from app.services.document.file_validator import validate_file

from app.services.document.pdf_service import read_pdf
from app.services.document.word_service import read_docx
from app.services.document.excel_service import read_excel
from app.services.document.csv_service import read_csv
from app.services.document.text_service import read_txt
from app.services.document.json_service import read_json
from app.services.document.ppt_service import read_ppt

LOADERS = {

    ".pdf": read_pdf,

    ".docx": read_docx,

    ".xlsx": read_excel,

    ".csv": read_csv,

    ".txt": read_txt,

    ".json": read_json,

    ".pptx": read_ppt,

}


def load_document(file_path):

    validate_file(file_path)

    ext = os.path.splitext(file_path)[1].lower()

    loader = LOADERS.get(ext)

    if loader is None:

        raise Exception("Unsupported file.")

    return loader(file_path)