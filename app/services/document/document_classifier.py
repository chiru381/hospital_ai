"""
document_classifier.py

Rule-based document classifier for RAG.
"""

import re
from typing import Dict


class DocumentClassifier:

    def __init__(self):

        self.categories = {

            "Hospital Policy": [

                "policy",
                "hospital policy",
                "guideline",
                "rules",
                "regulation",
                "procedure"

            ],

            "SOP": [

                "standard operating procedure",
                "sop",
                "workflow",
                "step",
                "process"

            ],

            "Lab Report": [

                "lab report",
                "laboratory",
                "cbc",
                "blood",
                "urine",
                "glucose",
                "hemoglobin",
                "test result"

            ],

            "Prescription": [

                "prescription",
                "rx",
                "medicine",
                "tablet",
                "capsule",
                "dosage",
                "doctor"

            ],

            "Discharge Summary": [

                "discharge",
                "diagnosis",
                "treatment",
                "admission",
                "patient summary"

            ],

            "Medical Guideline": [

                "clinical guideline",
                "treatment guideline",
                "recommendation",
                "protocol"

            ],

            "Invoice": [

                "invoice",
                "amount",
                "payment",
                "bill",
                "gst",
                "subtotal",
                "total"

            ],

            "Insurance": [

                "insurance",
                "claim",
                "coverage",
                "policy holder",
                "payer"

            ],

            "Patient Record": [

                "patient",
                "mrn",
                "age",
                "gender",
                "medical history",
                "diagnosis"

            ],

            "HR Document": [

                "employee",
                "salary",
                "leave",
                "attendance",
                "joining",
                "offer letter"

            ]

        }

    # ----------------------------------------------------
    # Clean Text
    # ----------------------------------------------------

    def preprocess(self, text: str) -> str:

        text = text.lower()

        text = re.sub(r"\s+", " ", text)

        return text

    # ----------------------------------------------------
    # Classify
    # ----------------------------------------------------

    def classify(self, text: str) -> Dict:

        text = self.preprocess(text)

        scores = {}

        for category, keywords in self.categories.items():

            score = 0

            for keyword in keywords:

                if keyword.lower() in text:

                    score += 1

            scores[category] = score

        best_category = max(
            scores,
            key=scores.get
        )

        confidence = scores[best_category]

        if confidence == 0:

            best_category = "Unknown"

        return {

            "document_type": best_category,

            "confidence_score": confidence,

            "scores": scores

        }