import os

# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")


class AppSettings(BaseSettings):
    project_name: str = "Send Mail API"
    project_host: str = "127.0.0.1"
    project_port: int = 8080

    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = dotenv_path


app_settings = AppSettings()