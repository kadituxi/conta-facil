from integrations.llm import LLMService
from integrations.ocr import OCRService
from integrations.whatsapp import WhatsAppClient


class ReceiptService:
    def __init__(self):
        self.ocr = OCRService()
        self.whatsapp = WhatsAppClient()
        self.llm = LLMService()

    def process_message(self, message_id: str) -> dict:
        file_path = self.whatsapp.get_media_as_file(message_id)

        ocr_text = self.ocr.extract_text(file_path)

        structured_data = self.llm.extract_transaction(ocr_text)

        return structured_data
