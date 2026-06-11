from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from schemas.transacao_schemas import TransacaoRead


class UtilizadorBase(BaseModel):
    nome: str = Field(..., max_length=255)
    telefone: str = Field(..., max_length=50)


class UtilizadorCreate(UtilizadorBase):
    pass


class UtilizadorRead(UtilizadorBase):
    id: int
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)


class UtilizadorDetail(UtilizadorRead):
    transacoes: list[TransacaoRead] = []
