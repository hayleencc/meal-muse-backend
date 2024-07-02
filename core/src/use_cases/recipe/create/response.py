from datetime import datetime
from typing import List, NamedTuple, Optional


class CreateRecipeResponse(NamedTuple):
    recipe_id: Optional[str]
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
    created_at: Optional[datetime | str]
    updated_at: Optional[datetime | str]
    is_archived: bool
