import pytest

from adapters.src.repositories import SQLRecipeRepository
from adapters.src.repositories.sql.config.session_manager import Session
from core.src.exceptions import RecipeRepositoryException
from core.src.models.recipe import Recipe


def test_list_recipe_in_sql_adapter_when_there_are_two_registers_should_return_a_list_of_two_recipes(
        mock_session_query_all_return_two_objects: Session, mock_recipe: Recipe):
    sql_repository = SQLRecipeRepository(session=mock_session_query_all_return_two_objects)

    recipes = sql_repository.list_all()

    assert len(recipes) > 0
    assert all(isinstance(recipe, Recipe) for recipe in recipes)


def test_list_recipe_in_sql_adapter_when_there_is_no_register(mock_session: Session):
    sql_repository = SQLRecipeRepository(session=mock_session)

    recipes = sql_repository.list_all()

    assert len(recipes) == 0


def test_list_recipe_in_sql_adapter_when_there_is_exception_should_raise_repository_exception(
        mock_session_query_exception: Session):
    sql_repository = SQLRecipeRepository(session=mock_session_query_exception)
    message = "Something was wrong trying to list_all the Recipe"

    with pytest.raises(RecipeRepositoryException, match=message):
        sql_repository.list_all()
