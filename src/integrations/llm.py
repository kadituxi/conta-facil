import json
import re

from google import genai

from config import settings
from schemas.transacao_schemas import TransacaoBase


def to_json(raw: str) -> dict:
    # remove markdown code blocks
    raw = re.sub(r"```json", "", raw)
    raw = re.sub(r"```", "", raw)
    raw = raw.strip()

    # extrai só o JSON (caso venha texto extra)
    start = raw.find("{")
    end = raw.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON found in response")

    json_str = raw[start : end + 1]

    return json.loads(json_str)


class LLMService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.google_api_key)

    def extract_transaction(self, ocr_text: str) -> str:
        prompt = f"""
Tu és um sistema especializado em extracção de dados financeiros a partir de textos de recibos, facturas e comprovativos.

A tua tarefa é extrair uma transacção financeira estruturada.

REGRAS OBRIGATÓRIAS:
- Responde APENAS com JSON válido
- NÃO uses markdown
- NÃO uses ``` ou qualquer formatação
- NÃO adiciones texto extra
- NÃO inventes informação
- Se algum campo não existir no texto, usa null

CAMPOS A EXTRAIR:
- tipo: deve ser "RECEITA" ou "DESPESA"
- valor: número (float)
- categoria: string curta (ex: alimentação, transporte, serviços, compras)
- descricao: explicação clara da transacção
- data: formato YYYY-MM-DD ou null se não existir

FORMATO DE RESPOSTA OBRIGATÓRIO:
Retorna EXCLUSIVAMENTE um JSON válido como este exemplo:

{{
  "tipo": "DESPESA",
  "valor": 0.0,
  "categoria": "string",
  "descricao": "string",
  "data": "YYYY-MM-DD ou null"
}}

TEXTO DE ENTRADA:
{ocr_text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": TransacaoBase,
            },
        )

        return to_json(response.text)
