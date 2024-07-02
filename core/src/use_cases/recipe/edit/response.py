from datetime import datetime
from typing import List, NamedTuple, Optional


class EditRecipeResponse(NamedTuple):
    recipe_id: str
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
    is_archived: bool
    created_at: Optional[datetime | str]
    updated_at: Optional[datetime | str]
