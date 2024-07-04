import datetime
import uuid

from sqlalchemy import JSON, Boolean, Column, DateTime, String

from .base import Base


class RecipeRecord(Base):
    __tablename__ = 'recipes'
    recipe_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    description = Column(String)
    ingredients = Column(JSON)
    steps = Column(JSON)
    image_url = Column(String)
    is_archived = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(DateTime, default=datetime.datetime.now(
        datetime.UTC), onupdate=datetime.datetime.now(datetime.UTC))
