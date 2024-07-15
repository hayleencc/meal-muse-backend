from core.src.repository import RecipeRepository
from core.src.use_cases import CreateRecipe, DeleteRecipe, EditRecipe, GetRecipeById, ListRecipe
from factories.repositories import sql_recipe_repository


def get_recipe_repository() -> RecipeRepository:
    return sql_recipe_repository()


def create_recipe_use_case() -> CreateRecipe:
    return CreateRecipe(recipe_repository=get_recipe_repository())


def list_recipes_use_case() -> ListRecipe:
    return ListRecipe(recipe_repository=get_recipe_repository())


def get_recipe_by_id_use_case() -> GetRecipeById:
    return GetRecipeById(recipe_repository=get_recipe_repository())


def edit_recipe_use_case() -> EditRecipe:
    return EditRecipe(recipe_repository=get_recipe_repository())


def delete_recipe_use_case() -> DeleteRecipe:
    return DeleteRecipe(recipe_repository=get_recipe_repository())
