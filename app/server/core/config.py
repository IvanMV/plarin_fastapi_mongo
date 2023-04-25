import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent.parent.parent
env_path = Path(BASE_DIR, ".env")

load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Plarin Test Task"
    PROJECT_VERSION: str = "1.0"
    MONGO_USER: str = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    MONGO_PASSWORD: str = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    MONGO_SERVER: str = os.getenv("MONGO_SERVER", "localhost")
    MONGO_PORT: str = os.getenv("MONGO_PORT", 27017)
    DATABASE_URL = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_SERVER}:{MONGO_PORT}/employees?authSource=admin"


settings = Settings()
