from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AnexoBase(BaseModel):
    caminho_ficheiro: str
    texto_ocr: str | None = None


class AnexoCreate(AnexoBase):
    pass


class AnexoRead(AnexoBase):
    id: int
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)
