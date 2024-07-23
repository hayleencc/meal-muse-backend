from datetime import datetime
from typing import List, NamedTuple, Optional


class CreateRecipeRequest(NamedTuple):
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_archived: Optional[bool] = False
