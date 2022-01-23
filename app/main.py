import asyncio
from fastapi import FastAPI
from api import router
from httpx import AsyncClient
from settings import get_settings

settings = get_settings()
app = FastAPI()


app.include_router(router, prefix="")