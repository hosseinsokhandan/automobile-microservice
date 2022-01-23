from fastapi import FastAPI
from api import router
from settings import get_settings
from tortoise.contrib.fastapi import register_tortoise
from database import TORTOISE_ORM

settings = get_settings()
app = FastAPI()


app.include_router(router, prefix="/automobile")

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)
