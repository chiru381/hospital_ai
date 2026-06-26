import hashlib
from pathlib import Path
from typing import Set


class DuplicateDetector:
    """
    Detect duplicate documents using file hashes or text hashes.
    """

    def __init__(self):
        self.file_hashes: Set[str] = set()
        self.text_hashes: Set[str] = set()

    # ---------------------------------------------------------
    # Hash Functions
    # ---------------------------------------------------------

    @staticmethod
    def md5_hash(data: bytes) -> str:
        return hashlib.md5(data).hexdigest()

    @staticmethod
    def sha256_hash(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    # ---------------------------------------------------------
    # File Hash
    # ---------------------------------------------------------

    def get_file_hash(self, file_path: str) -> str:
        """
        Generate SHA256 hash for a file.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(file_path)

        hasher = hashlib.sha256()

        with open(path, "rb") as file:

            while True:

                chunk = file.read(8192)

                if not chunk:
                    break

                hasher.update(chunk)

        return hasher.hexdigest()

    # ---------------------------------------------------------
    # Text Hash
    # ---------------------------------------------------------

    def get_text_hash(self, text: str) -> str:
        """
        Generate SHA256 hash for extracted text.
        """

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    # ---------------------------------------------------------
    # Duplicate File Check
    # ---------------------------------------------------------

    def is_duplicate_file(self, file_path: str) -> bool:

        file_hash = self.get_file_hash(file_path)

        return file_hash in self.file_hashes

    def add_file(self, file_path: str):

        file_hash = self.get_file_hash(file_path)

        self.file_hashes.add(file_hash)

    # ---------------------------------------------------------
    # Duplicate Text Check
    # ---------------------------------------------------------

    def is_duplicate_text(self, text: str) -> bool:

        text_hash = self.get_text_hash(text)

        return text_hash in self.text_hashes

    def add_text(self, text: str):

        text_hash = self.get_text_hash(text)

        self.text_hashes.add(text_hash)

    # ---------------------------------------------------------
    # Generic Check
    # ---------------------------------------------------------

    def check_file(self, file_path: str) -> bool:
        """
        Returns True if duplicate.
        Otherwise stores hash and returns False.
        """

        file_hash = self.get_file_hash(file_path)

        if file_hash in self.file_hashes:
            return True

        self.file_hashes.add(file_hash)

        return False

    def check_text(self, text: str) -> bool:
        """
        Returns True if duplicate.
        Otherwise stores hash and returns False.
        """

        text_hash = self.get_text_hash(text)

        if text_hash in self.text_hashes:
            return True

        self.text_hashes.add(text_hash)

        return False

    # ---------------------------------------------------------
    # Reset Cache
    # ---------------------------------------------------------

    def clear(self):

        self.file_hashes.clear()

        self.text_hashes.clear()

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def stats(self):

        return {

            "stored_files": len(self.file_hashes),

            "stored_documents": len(self.text_hashes)

        }