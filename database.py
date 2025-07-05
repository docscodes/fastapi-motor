from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config import BaseConfig


settings = BaseConfig()
motor_client = AsyncIOMotorClient(settings.DB_URL)
database = motor_client["fastapi-motor"]



def get_database() -> AsyncIOMotorDatabase:
    return database
