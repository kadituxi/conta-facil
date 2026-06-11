from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from models.models import TipoTransacao
from schemas.anexo_schemas import AnexoRead


class TransacaoBase(BaseModel):
    tipo: TipoTransacao
    valor: float
    descricao: str | None = None
    categoria: str | None = None
    data_transacao: date


class TransacaoCreate(TransacaoBase):
    utilizador_id: int


class TransacaoRead(TransacaoBase):
    id: int
    utilizador_id: int
    criado_em: datetime
    anexos: list[AnexoRead] = []

    model_config = ConfigDict(from_attributes=True)
