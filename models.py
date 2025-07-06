from datetime import datetime
from typing import Annotated
from bson import ObjectId
from pydantic import BaseModel, Field, BeforeValidator


# Helper to parse ObjectId to/from string
def parse_object_id(value: str | ObjectId) -> str:
    if isinstance(value, ObjectId):
        return str(value)
    return str(value)

# Annotated type for ObjectId fields
PyObjectId = Annotated[str, BeforeValidator(parse_object_id)]

class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=lambda: str(ObjectId()), alias="_id")

    class Config:
        populate_by_name = True  # Allows using `id` when creating models
        json_encoders = {ObjectId: str}


class CommentBase(BaseModel):
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    pass


class PostBase(MongoBaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    comments: list[Comment] = Field(default_factory=list)
