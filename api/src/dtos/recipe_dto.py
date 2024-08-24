from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Recipe(BaseModel):
    title: Optional[str]
    description: Optional[str]
    ingredients: Optional[List[str]]
    steps: Optional[List[str]]
    image_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_archived: Optional[bool] = False
    recipe_id: Optional[str] = None
