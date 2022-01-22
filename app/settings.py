from functools import lru_cache
from pydantic import BaseSettings, Field, PostgresDsn, validator
from typing import Optional, Any, Dict, List


class Settings(BaseSettings):
    DISCOVERY_URL: str
    SERVICE_NAME: str
    
    DB_SCHEME: str = Field(default="postgres")
    DB_HOST: str = Field(default="postgres")
    DB_PORT: str = Field(default="5432")
    DB_NAME: str = Field(default="automobile")
    DB_USER: str = Field(default="automobile")
    DB_PASSWD: str = Field(default="123456")

    MODELS: List = [
        "models.Automobile",
        # "models.Part",
        "aerich.models",  # aerich
    ]

    DATABASE_URL: Optional[PostgresDsn] = None

    @validator("DATABASE_URL", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme=values["DB_SCHEME"],
            user=values["DB_USER"],
            password=values["DB_PASSWD"],
            host=values["DB_HOST"],
            port=values["DB_PORT"],
            path=f"/{values['DB_NAME']}",
        )

    class Config:
        case_sensitive: bool = True
        env_file: str = ".env"

    class Config:
        case_sensitive: bool = True
        env_file: str = "../.env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
