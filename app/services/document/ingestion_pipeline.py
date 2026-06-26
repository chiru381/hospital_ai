"""
ingestion_pipeline.py

Complete document ingestion pipeline.
"""

import uuid
from pathlib import Path

from app.services.document.file_validator import validate_file
from app.services.document.document_loader import load_document
from app.services.document.metadata_service import get_metadata
from app.services.document.document_cleaner import DocumentCleaner
from app.services.document.duplicate_detector import DuplicateDetector
from app.services.document.language_detector import LanguageDetector
from app.services.document.keyword_extractor import KeywordExtractor
from app.services.document.document_classifier import DocumentClassifier
from app.services.document.document_summary import DocumentSummary
from app.services.document.chunk_service import chunk_text
from app.services.document.embedding_service import generate_embeddings
from app.services.document.vector_store import save_vectors


class IngestionPipeline:

    def __init__(self):

        self.cleaner = DocumentCleaner()

        self.duplicate_detector = DuplicateDetector()

        self.language_detector = LanguageDetector()

        self.keyword_extractor = KeywordExtractor()

        self.classifier = DocumentClassifier()

        self.summarizer = DocumentSummary()

    # --------------------------------------------------------

    def ingest(self, file_path: str):

        file_path = Path(file_path)

        # ----------------------------------------------
        # Validate
        # ----------------------------------------------

        validate_file(file_path)

        # ----------------------------------------------
        # Duplicate File
        # ----------------------------------------------

        if self.duplicate_detector.check_file(str(file_path)):

            return {

                "success": False,

                "message": "Duplicate file."

            }

        # ----------------------------------------------
        # Read Document
        # ----------------------------------------------

        text = load_document(str(file_path))

        # ----------------------------------------------
        # Clean
        # ----------------------------------------------

        text = self.cleaner.clean(text)

        # ----------------------------------------------
        # Duplicate Text
        # ----------------------------------------------

        if self.duplicate_detector.check_text(text):

            return {

                "success": False,

                "message": "Duplicate document content."

            }

        # ----------------------------------------------
        # Metadata
        # ----------------------------------------------

        metadata = get_metadata(str(file_path))

        # ----------------------------------------------
        # Language
        # ----------------------------------------------

        language = self.language_detector.analyze(text)

        # ----------------------------------------------
        # Keywords
        # ----------------------------------------------

        keywords = self.keyword_extractor.analyze(text)

        # ----------------------------------------------
        # Classification
        # ----------------------------------------------

        classification = self.classifier.classify(text)

        # ----------------------------------------------
        # Summary
        # ----------------------------------------------

        summary = self.summarizer.summarize_document(text)

        # ----------------------------------------------
        # Chunk
        # ----------------------------------------------

        chunks = chunk_text(text)

        # ----------------------------------------------
        # Embeddings
        # ----------------------------------------------

        embeddings = generate_embeddings(chunks)

        # ----------------------------------------------
        # Prepare Payload
        # ----------------------------------------------

        payloads = []

        for chunk in chunks:

            payloads.append({

                "id": str(uuid.uuid4()),

                "filename": file_path.name,

                "text": chunk,

                "summary": summary["summary"],

                "language": language["language_code"],

                "language_name": language["language_name"],

                "keywords": keywords["tags"],

                "document_type": classification["document_type"],

                "metadata": metadata

            })

        # ----------------------------------------------
        # Save to Qdrant
        # ----------------------------------------------

        save_vectors(

            chunks=chunks,

            vectors=embeddings,

            payloads=payloads

        )

        # ----------------------------------------------

        return {

            "success": True,

            "filename": file_path.name,

            "metadata": metadata,

            "language": language,

            "classification": classification,

            "keywords": keywords,

            "summary": summary,

            "chunks": len(chunks)

        }