from core.src.exceptions import RecipeBusinessException, RecipeRepositoryException
from core.src.repository import RecipeRepository
from core.src.use_cases.recipe.list.response import ListRecipeResponse


class ListRecipe:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def __call__(self) -> ListRecipeResponse:
        try:
            response = self.recipe_repository.list_all()
            return ListRecipeResponse(recipes=response)

        except RecipeRepositoryException as e:
            raise RecipeBusinessException(str(e))
