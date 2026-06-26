"""
document_summary.py

Generate summaries for documents using Hugging Face Transformers.
"""

from typing import Dict
from transformers import pipeline


class DocumentSummary:

    def __init__(self):

        self.summarizer = pipeline(
            task="summarization",
            model="facebook/bart-large-cnn"
        )

    # ---------------------------------------------------------
    # Clean Text
    # ---------------------------------------------------------

    def preprocess(self, text: str) -> str:

        text = " ".join(text.split())

        return text

    # ---------------------------------------------------------
    # Summarize
    # ---------------------------------------------------------

    def summarize(
        self,
        text: str,
        max_length: int = 180,
        min_length: int = 50
    ) -> str:

        text = self.preprocess(text)

        if len(text) < 100:

            return text

        # BART supports about 1024 tokens
        text = text[:3500]

        summary = self.summarizer(

            text,

            max_length=max_length,

            min_length=min_length,

            do_sample=False

        )

        return summary[0]["summary_text"]

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def summarize_document(
        self,
        text: str
    ) -> Dict:

        summary = self.summarize(text)

        return {

            "summary": summary,

            "original_length": len(text),

            "summary_length": len(summary)

        }