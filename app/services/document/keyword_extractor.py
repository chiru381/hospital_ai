"""
keyword_extractor.py

Extract important keywords from documents.
"""

from typing import List, Dict
from keybert import KeyBERT


class KeywordExtractor:

    def __init__(self):

        self.model = KeyBERT(
            model="all-MiniLM-L6-v2"
        )

    # --------------------------------------------------------
    # Extract Keywords
    # --------------------------------------------------------

    def extract_keywords(
        self,
        text: str,
        top_n: int = 10,
        min_ngram: int = 1,
        max_ngram: int = 2
    ) -> List[Dict]:

        if not text.strip():

            return []

        keywords = self.model.extract_keywords(

            text,

            keyphrase_ngram_range=(
                min_ngram,
                max_ngram
            ),

            stop_words="english",

            top_n=top_n

        )

        results = []

        for word, score in keywords:

            results.append({

                "keyword": word,

                "score": round(float(score), 4)

            })

        return results

    # --------------------------------------------------------
    # Extract Only Keyword Names
    # --------------------------------------------------------

    def get_keyword_list(
        self,
        text: str,
        top_n: int = 10
    ) -> List[str]:

        keywords = self.extract_keywords(
            text=text,
            top_n=top_n
        )

        return [

            item["keyword"]

            for item in keywords

        ]

    # --------------------------------------------------------
    # Extract Tags
    # --------------------------------------------------------

    def generate_tags(
        self,
        text: str,
        top_n: int = 5
    ) -> List[str]:

        return self.get_keyword_list(
            text,
            top_n
        )

    # --------------------------------------------------------
    # Full Analysis
    # --------------------------------------------------------

    def analyze(
        self,
        text: str
    ) -> Dict:

        keywords = self.extract_keywords(text)

        return {

            "total_keywords": len(keywords),

            "keywords": keywords,

            "tags": [

                item["keyword"]

                for item in keywords[:5]

            ]

        }