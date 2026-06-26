import re
import unicodedata
from typing import List


class DocumentCleaner:

    def __init__(self):
        pass

    def normalize_unicode(self, text: str) -> str:
        """
        Normalize unicode characters.
        """
        return unicodedata.normalize("NFKC", text)

    def remove_non_printable(self, text: str) ->str:
        """
        Remove non printable ASCII characters.
        """
        return "".join(
            ch
            for ch in text
            if ch.isprintable() or ch == "\n"
        )

    def remove_tabs(self, text: str) -> str:
        """
        Replace tabs with spaces.
        """
        return text.replace("\t", " ")

    def remove_extra_spaces(self, text: str) -> str:
        """
        Remove duplicate spaces.
        """
        return re.sub(r"[ ]{2,}", " ", text)

    def remove_blank_lines(self, text: str) -> str:
        """
        Remove multiple blank lines.
        """
        return re.sub(r"\n{3,}", "\n\n", text)

    def remove_page_numbers(self, text: str) -> str:
        """
        Remove page numbers.

        Example:
        Page 1
        Page 25
        PAGE 7
        """
        pattern = r"(?im)^page\s+\d+\s*$"

        return re.sub(pattern, "", text)

    def remove_headers_footers(
        self,
        text: str,
        keywords: List[str] = None
    ) -> str:
        """
        Remove common headers and footers.
        """

        if keywords is None:

            keywords = [

                "Confidential",

                "Hospital Policy",

                "Internal Use Only",

                "Page",

                "Copyright",

                "All Rights Reserved"

            ]

        lines = text.splitlines()

        cleaned = []

        for line in lines:

            line_strip = line.strip()

            remove = False

            for keyword in keywords:

                if keyword.lower() in line_strip.lower():

                    remove = True

                    break

            if not remove:

                cleaned.append(line)

        return "\n".join(cleaned)

    def remove_duplicate_lines(self, text: str) -> str:
        """
        Remove repeated consecutive lines.
        """

        lines = text.splitlines()

        cleaned = []

        previous = None

        for line in lines:

            if line.strip() != previous:

                cleaned.append(line)

                previous = line.strip()

        return "\n".join(cleaned)

    def strip_lines(self, text: str) -> str:
        """
        Remove leading and trailing spaces from every line.
        """

        return "\n".join(

            line.strip()

            for line in text.splitlines()

        )

    def clean(self, text: str) -> str:
        """
        Run complete cleaning pipeline.
        """

        text = self.normalize_unicode(text)

        text = self.remove_non_printable(text)

        text = self.remove_tabs(text)

        text = self.remove_page_numbers(text)

        text = self.remove_headers_footers(text)

        text = self.remove_duplicate_lines(text)

        text = self.strip_lines(text)

        text = self.remove_extra_spaces(text)

        text = self.remove_blank_lines(text)

        return text.strip()