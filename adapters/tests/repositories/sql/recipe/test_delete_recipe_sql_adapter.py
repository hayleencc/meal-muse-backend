import pytest

from adapters.src.repositories import SQLRecipeRepository
from adapters.src.repositories.sql.config.session_manager import Session
from core.src.exceptions import RecipeRepositoryException
from core.src.models import Recipe


def test_delete_recipe_when_it_is_found_should_return_deleted_recipe(
        mock_session_query_delete_recipe: Session, mock_recipe: Recipe):
    recipe_sql_repository = SQLRecipeRepository(session=mock_session_query_delete_recipe)

    deleted_recipe = recipe_sql_repository.delete(recipe_id=mock_recipe.recipe_id)

    assert deleted_recipe is True


def test_delete_recipe_when_exception_occurs_should_raise_repository_exception(
        mock_session_query_exception: Session, mock_recipe: Recipe):
    recipe_sql_repository = SQLRecipeRepository(session=mock_session_query_exception)
    message = "Something was wrong trying to delete the Recipe"

    with pytest.raises(RecipeRepositoryException, match=message):
        recipe_sql_repository.delete(recipe_id=mock_recipe.recipe_id)
