from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str


class PDFUploadResponse(BaseModel):
    filename: str
    status: str