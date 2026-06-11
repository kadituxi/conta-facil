from __future__ import annotations

import enum
from datetime import UTC, date, datetime

from sqlalchemy import Date, DateTime, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class TipoTransacao(enum.Enum):
    RECEITA = "receita"
    DESPESA = "despesa"


class Utilizador(Base):
    __tablename__ = "utilizadores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    telefone: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    transacoes: Mapped[list["Transacao"]] = relationship(
        back_populates="utilizador", cascade="all, delete-orphan"
    )
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )


class Transacao(Base):
    __tablename__ = "transacoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    utilizador_id: Mapped[int] = mapped_column(
        ForeignKey("utilizadores.id"), nullable=False
    )
    tipo: Mapped[TipoTransacao] = mapped_column(Enum(TipoTransacao), nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    descricao: Mapped[str | None] = mapped_column(String(500), nullable=True)
    categoria: Mapped[str | None] = mapped_column(String(100), nullable=True)
    data_transacao: Mapped[date] = mapped_column(Date, nullable=False)
    utilizador: Mapped["Utilizador"] = relationship(back_populates="transacoes")
    anexos: Mapped[list["Anexo"]] = relationship(
        back_populates="transacao", cascade="all, delete-orphan"
    )
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )


class Anexo(Base):
    __tablename__ = "anexos"

    id: Mapped[int] = mapped_column(primary_key=True)
    transacao_id: Mapped[int] = mapped_column(
        ForeignKey("transacoes.id"), nullable=False
    )
    caminho_ficheiro: Mapped[str] = mapped_column(Text, nullable=False)
    texto_ocr: Mapped[str | None] = mapped_column(Text, nullable=True)
    transacao: Mapped["Transacao"] = relationship(back_populates="anexos")
    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
