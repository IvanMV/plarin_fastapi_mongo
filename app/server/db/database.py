import motor.motor_asyncio
from beanie import init_beanie
from server.core.config import settings
from server.db.models.employees import Employees


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(database=client.db_staff, document_models=[Employees])
