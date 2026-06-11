import base64

import requests

from config import settings

API_KEY = settings.api_key.get_secret_value()
BASE_URL = settings.base_url
INSTANCE_NAME = settings.instance_name


class WhatsAppClient:
    def __init__(self):
        self.headers = {"apikey": API_KEY}

    def send_text(self, number: str, text: str):
        body = {"number": number, "text": text}

        return requests.post(
            f"{BASE_URL}/message/sendText/{INSTANCE_NAME}",
            json=body,
            headers=self.headers,
        )

    def get_media_as_file(self, message_id: str) -> str:
        body = {"message": {"key": {"id": message_id}}}

        response = requests.post(
            f"{BASE_URL}/chat/getBase64FromMediaMessage/{INSTANCE_NAME}",
            json=body,
            headers=self.headers,
        )

        data = response.json()

        file_path = data["fileName"]

        with open(file_path, "wb") as f:
            f.write(base64.b64decode(data["base64"]))

        return file_path
