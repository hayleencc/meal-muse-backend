from typing import List, NamedTuple, Optional


class Recipe(NamedTuple):
    recipe_id: str
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: str
    created_at: str
    updated_at: Optional[str]
