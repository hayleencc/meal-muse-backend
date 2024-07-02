from typing import Optional

from core.src.exceptions import (
    RecipeBusinessException,
    RecipeNoneException,
    RecipeNotFoundException,
    RecipeRepositoryException,
)
from core.src.models import Recipe
from core.src.repository import RecipeRepository
from core.src.use_cases.recipe.edit.request import EditRecipeRequest
from core.src.use_cases.recipe.edit.response import EditRecipeResponse


class EditRecipe():
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def __call__(self, request: EditRecipeRequest) -> Optional[EditRecipeResponse]:
        try:
            recipe = self.recipe_repository.get_by_id(request.recipe_id)
            if recipe is None:
                raise RecipeNotFoundException(recipe_id=request.recipe_id)
            updated_recipe = Recipe(**{**recipe._asdict(), **request._asdict()})
            response = self.recipe_repository.edit(updated_recipe)

            if not response:
                raise RecipeNoneException()

            return EditRecipeResponse(**response._asdict())
        except RecipeRepositoryException as e:
            raise RecipeBusinessException(str(e))
