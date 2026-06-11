from integrations.whatsapp import WhatsAppClient


class MessageService:
    def __init__(self):
        self.whatsapp = WhatsAppClient()

    def send_welcome(self, number: str):
        self.whatsapp.send_text(number, "Olá 👋 Bem-vindo ao Conta Fácil!")
