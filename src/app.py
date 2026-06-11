from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.db import engine


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Startup
    yield
    # Shutdown
    await engine.dispose()


app = FastAPI(
    title="Conta Fácil API",
    description="API para gestão de receitas e desepesas financeiras por meio do WhatsApp",
    version="1.0.0",
    lifespan=lifespan,
)
