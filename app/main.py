import asyncio
from fastapi import FastAPI
from api import router
from httpx import AsyncClient
from settings import get_settings

settings = get_settings()
app = FastAPI()


app.include_router(router)


@app.on_event("startup")
async def startup_event():
    """register your self at service discovery"""
    async with AsyncClient() as client:
        data = {"name": settings.SERVICE_NAME}
        resp = await client.post(settings.DISCOVERY_URL, json=data)
        print(resp.text)
        if resp.is_success is False:
            await asyncio.sleep(2)
            startup_event()


@app.on_event("shutdown")
async def shutdown_event():
    """unregister your self from service discovery"""
