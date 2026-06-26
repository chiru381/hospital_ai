import os

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".xlsx",
    ".csv",
    ".pptx",
    ".txt",
    ".json",
}

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB


def validate_file(file_path):

    if not os.path.exists(file_path):
        raise Exception("File not found.")

    ext = os.path.splitext(file_path)[1].lower()

    if ext not in SUPPORTED_EXTENSIONS:
        raise Exception(f"{ext} is not supported.")

    size = os.path.getsize(file_path)

    if size > MAX_FILE_SIZE:
        raise Exception("File size exceeds 20MB.")

    return True