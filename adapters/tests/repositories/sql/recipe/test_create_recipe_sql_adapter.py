from adapters.src.repositories import SQLRecipeRepository
from adapters.src.repositories.sql.config.session_manager import Session
from core.src.models import Recipe


def test_create_recipe_in_sql_adapter_should_return_created_recipe(mock_session: Session, mock_recipe: Recipe):
    sql_repository = SQLRecipeRepository(session=mock_session)
    created_recipe = sql_repository.create(mock_recipe)
    assert created_recipe is not None
    assert isinstance(created_recipe, Recipe)
