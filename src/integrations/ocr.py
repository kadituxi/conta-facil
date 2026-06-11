from pathlib import Path

import pytesseract
from PIL import Image


class OCRService:
    def extract_text(self, file: Path | str) -> str:
        img = Image.open(file)
        return pytesseract.image_to_string(img)
