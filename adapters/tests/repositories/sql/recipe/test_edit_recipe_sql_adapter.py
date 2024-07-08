import pytest

from adapters.src.repositories import SQLRecipeRepository
from adapters.src.repositories.sql.config.session_manager import Session
from core.src.exceptions import RecipeRepositoryException
from core.src.models import Recipe


def test_edit_recipe_when_it_is_found_should_return_updated_recipe(
        mock_session: Session, mock_updated_recipe: Recipe):
    recipe_sql_repository = SQLRecipeRepository(session=mock_session)

    updated_recipe = recipe_sql_repository.edit(updated_recipe=mock_updated_recipe)

    assert updated_recipe is not None
    assert isinstance(updated_recipe, Recipe)
    assert updated_recipe == mock_updated_recipe


def test_edit_recipe_when_exception_occurs_should_raise_repository_exception(
        mock_session_query_exception: Session, mock_updated_recipe: Recipe):
    recipe_sql_repository = SQLRecipeRepository(session=mock_session_query_exception)
    message = "Something was wrong trying to edit the Recipe"

    with pytest.raises(RecipeRepositoryException, match=message):
        recipe_sql_repository.edit(updated_recipe=mock_updated_recipe)
