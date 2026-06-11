from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    base_dir: Path = Path(__file__).parent
    secret_key: SecretStr
    max_upload_size_bytes: int = 5 * 1024 * 1024

    database_url: str

    mail_server: str
    mail_port: int
    mail_username: str
    mail_password: SecretStr
    mail_from: str
    mail_use_tls: bool
    frontend_url: str


settings = Settings()  # type: ignore[call-arg]
