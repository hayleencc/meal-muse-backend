from datetime import datetime
from typing import List, NamedTuple, Optional


class CreateRecipeRequest(NamedTuple):
    title: Optional[str]
    description: Optional[str]
    ingredients: Optional[List[str]]
    steps: Optional[List[str]]
    image_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    recipe_id: Optional[str] = None
    is_archived: Optional[bool] = False
