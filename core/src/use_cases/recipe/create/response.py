from typing import List, NamedTuple, Optional


class CreateRecipeResponse(NamedTuple):
    recipe_id: Optional[str]
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
    created_at: str
    updated_at: Optional[str]
