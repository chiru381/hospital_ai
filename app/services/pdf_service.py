import os

from pypdf import PdfReader

def load_pdf_text(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def load_all_pdfs(folder):

    documents = []

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            full_path = os.path.join(folder, file)

            text = load_pdf_text(full_path)

            documents.append({
                "file": file,
                "content": text
            })

    return documents