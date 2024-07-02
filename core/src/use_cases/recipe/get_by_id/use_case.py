from typing import Optional

from core.src.exceptions import (
    RecipeBusinessException,
    RecipeNotFoundException,
    RecipeRepositoryException,
)
from core.src.models import Recipe
from core.src.repository import RecipeRepository
from core.src.use_cases.recipe.get_by_id import GetRecipeByIdRequest, GetRecipeByIdResponse


class GetRecipeById:
    def __init__(self, recipe_respository: RecipeRepository):
        self.recipe_respository = recipe_respository

    def __validate__if_recipe_exists(self, recipe: Optional[Recipe], recipe_id: str) -> None:
        if not recipe:
            raise RecipeNotFoundException(recipe_id=recipe_id)

    def __call__(self, request: GetRecipeByIdRequest) -> GetRecipeByIdResponse:
        try:
            recipe = self.recipe_respository.get_by_id(request.recipe_id)
            self.__validate__if_recipe_exists(recipe, request.recipe_id)
            response = GetRecipeByIdResponse(**recipe._asdict())  # type: ignore
            return response

        except RecipeRepositoryException as e:
            raise RecipeBusinessException(str(e))
