from fastapi import FastAPI
from api import router


app = FastAPI()


app.include_router(router)


@app.on_event("startup")
async def startup_event():
    """register your self at service discovery"""


@app.on_event("shutdown")
async def shutdown_event():
    """unregister your self from service discovery"""
