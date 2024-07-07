import pytest

from adapters.src.repositories import SQLRecipeRepository
from adapters.src.repositories.sql.config.session_manager import Session
from core.src.exceptions import RecipeRepositoryException
from core.src.models import Recipe


def test_get_by_id_recipe_when_recipe_exists_should_return_recipe(
        mock_session: Session, mock_recipe: Recipe):
    recipe_sql_repository = SQLRecipeRepository(session=mock_session)

    recipe_found = recipe_sql_repository.get_by_id(recipe_id=mock_recipe.recipe_id)

    assert recipe_found is not None
    assert isinstance(recipe_found, Recipe)


def test_get_by_id_recipe_when_recipe_not_exists_should_return_none(
        mock_session_query_get_by_id_return_none: Session, mock_recipe: Recipe):
    recipe_sql_repository = SQLRecipeRepository(
        session=mock_session_query_get_by_id_return_none)

    recipe_found = recipe_sql_repository.get_by_id(recipe_id=mock_recipe.recipe_id)

    assert recipe_found is None


def test_get_by_id_recipe_when_exception_occurs_should_raise_repository_exception(
        mock_session_query_exception: Session):
    recipe_sql_repository = SQLRecipeRepository(session=mock_session_query_exception)
    message = "Something was wrong trying to get_by_id the Recipe"
    with pytest.raises(RecipeRepositoryException, match=message):
        recipe_sql_repository.get_by_id(recipe_id="1")
