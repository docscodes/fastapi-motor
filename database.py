from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


motor_client = AsyncIOMotorClient("mongodb://localhost:27017")
database = motor_client["fastapi-motor"]


def get_database() -> AsyncIOMotorDatabase:
    return database
