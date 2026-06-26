"""
language_detector.py

Detect document language before chunking/embedding.
"""

from typing import Dict, List
from langdetect import detect, detect_langs, DetectorFactory

# Make detection deterministic
DetectorFactory.seed = 0


class LanguageDetector:

    def __init__(self):

        self.language_names = {

            "en": "English",
            "hi": "Hindi",
            "te": "Telugu",
            "ta": "Tamil",
            "kn": "Kannada",
            "ml": "Malayalam",
            "mr": "Marathi",
            "gu": "Gujarati",
            "bn": "Bengali",
            "pa": "Punjabi",
            "ur": "Urdu",

            "fr": "French",
            "de": "German",
            "es": "Spanish",
            "it": "Italian",
            "pt": "Portuguese",
            "ru": "Russian",
            "ja": "Japanese",
            "ko": "Korean",
            "zh-cn": "Chinese",
            "ar": "Arabic"

        }

    # --------------------------------------------------
    # Detect Language Code
    # --------------------------------------------------

    def detect_language(self, text: str) -> str:

        if not text or len(text.strip()) < 10:

            return "unknown"

        try:

            return detect(text)

        except Exception:

            return "unknown"

    # --------------------------------------------------
    # Detect Language Name
    # --------------------------------------------------

    def detect_language_name(self, text: str) -> str:

        code = self.detect_language(text)

        return self.language_names.get(code, code)

    # --------------------------------------------------
    # Confidence Scores
    # --------------------------------------------------

    def detect_confidence(self, text: str) -> List[Dict]:

        if not text or len(text.strip()) < 10:

            return []

        try:

            results = detect_langs(text)

            output = []

            for lang in results:

                output.append({

                    "language_code": lang.lang,

                    "language_name": self.language_names.get(
                        lang.lang,
                        lang.lang
                    ),

                    "confidence": round(lang.prob, 4)

                })

            return output

        except Exception:

            return []

    # --------------------------------------------------
    # Full Detection
    # --------------------------------------------------

    def analyze(self, text: str) -> Dict:

        language = self.detect_language(text)

        return {

            "language_code": language,

            "language_name": self.language_names.get(
                language,
                language
            ),

            "confidence": self.detect_confidence(text)

        }

    # --------------------------------------------------
    # Multiple Documents
    # --------------------------------------------------

    def analyze_documents(self, documents: List[str]) -> List[Dict]:

        results = []

        for index, document in enumerate(documents):

            results.append({

                "document": index + 1,

                **self.analyze(document)

            })

        return results