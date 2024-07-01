from typing import List, NamedTuple, Optional


class CreateRecipeRequest(NamedTuple):
    recipe_id: Optional[str]
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image_url: Optional[str]
