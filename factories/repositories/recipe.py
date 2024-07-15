from adapters.src.repositories import MemoryRecipeRepository, SessionManager, SQLRecipeRepository
from core.src.repository import RecipeRepository


def memory_recipe_repository() -> RecipeRepository:
    return MemoryRecipeRepository()


def sql_recipe_repository() -> RecipeRepository:
    return SQLRecipeRepository(session=SessionManager.get_session())
