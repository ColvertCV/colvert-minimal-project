from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import List

class Settings(BaseSettings):
    # API settings
    title: str = Field(default="Colvert API")
    description: str = Field(default="API for Colvert")
    version: str = Field(default="1.0.0")
    debug: bool = Field(default=True)
    root_path: str = Field(default="")

    # CORS settings
    cors_allow_origins: List[str] = Field(default=["*"])
    cors_allow_credentials: bool = Field(default=True)
    cors_allow_methods: List[str] = Field(default=["*"])
    cors_allow_headers: List[str] = Field(default=["*"])
    cors_expose_headers: List[str] = Field(default=["*"])
    cors_max_age: int = Field(default=3600)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    @field_validator("cors_allow_origins", "cors_allow_methods", "cors_allow_headers", "cors_expose_headers", mode="before")
    def validate_list_fields(cls, v):
        if isinstance(v, str):
            if v.startswith("[") and v.endswith("]"):
                import json
                return json.loads(v)
            return [v]
        return v

settings = Settings()
