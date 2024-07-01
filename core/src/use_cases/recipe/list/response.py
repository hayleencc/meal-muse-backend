from typing import List, NamedTuple

from core.src.models import Recipe


class ListRecipeResponse(NamedTuple):
    recipes: List[Recipe]
