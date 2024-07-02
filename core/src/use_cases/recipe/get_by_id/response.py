from datetime import datetime
from typing import List, NamedTuple, Optional


class GetRecipeByIdResponse(NamedTuple):
    recipe_id: str
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
