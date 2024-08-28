from core.src.exceptions import (
    RecipeBusinessException,
    RecipeNotFoundException,
    RecipeRepositoryException,
)
from core.src.repository import RecipeRepository
from core.src.use_cases.recipe.delete.request import DeleteRecipeRequest
from core.src.use_cases.recipe.delete.response import DeleteRecipeResponse


class DeleteRecipe():
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def __call__(self, request: DeleteRecipeRequest) -> DeleteRecipeResponse:
        try:
            recipe = self.recipe_repository.get_by_id(request.recipe_id)
            if recipe is None:
                raise RecipeNotFoundException(recipe_id=request.recipe_id)
            response = self.recipe_repository.delete(request.recipe_id)
            return DeleteRecipeResponse(is_archived=bool(response))
        except RecipeRepositoryException as e:
            raise RecipeBusinessException(str(e))
