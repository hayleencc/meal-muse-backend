from datetime import datetime
from typing import List, NamedTuple, Optional


class EditRecipeRequest(NamedTuple):
    recipe_id: str
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
    updated_at: Optional[datetime | str]
