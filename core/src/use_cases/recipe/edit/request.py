from typing import List, NamedTuple, Optional


class EditRecipeRequest(NamedTuple):
    recipe_id: str
    title: Optional[str] = None
    description: Optional[str] = None
    steps: Optional[List[str]] = None
    ingredients: Optional[List[str]] = None
    image_url: Optional[str] = None
