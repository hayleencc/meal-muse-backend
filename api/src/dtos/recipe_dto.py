from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Recipe(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_archived: Optional[bool] = False
    recipe_id: Optional[str] = None
