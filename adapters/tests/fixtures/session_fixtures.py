from unittest.mock import MagicMock, create_autospec

import pytest
from sqlalchemy.orm import Session

from adapters.src.repositories.sql import RecipeRecord


@pytest.fixture(scope='function')
def mock_session():
    return MagicMock(spec=Session)


@pytest.fixture(scope='function')
def mock_session_commit_exception() -> MagicMock:
    mock = MagicMock(spec=Session)
    mock.commit.side_effect = Exception
    return mock


@pytest.fixture(scope='function')
def mock_session_query_exception() -> MagicMock:
    mock = MagicMock(spec=Session)
    mock.query.side_effect = Exception
    return mock


@pytest.fixture(scope='function')
def mock_session_query_all_return_no_objects() -> MagicMock:
    mock_session = MagicMock(spec=Session)
    mock_query = MagicMock()
    mock_session.query.return_value = mock_query
    mock_query.filter.return_value = mock_query
    mock_query.all.return_value = []
    return mock_session


@pytest.fixture(scope='function')
def mock_session_query_all_return_two_objects() -> MagicMock:
    mock_session = MagicMock(spec=Session)
    mock_query = MagicMock()
    mock_session.query.return_value = mock_query
    mock_query.filter.return_value = mock_query
    mock_query.all.return_value = [MagicMock(), MagicMock()]
    return mock_session


@pytest.fixture(scope='function')
def mock_session_query_get_by_id_return_none() -> MagicMock:
    mock_session = MagicMock(spec=Session)
    mock_query = MagicMock()
    mock_session.query.return_value = mock_query
    mock_query.filter.return_value = mock_query
    mock_query.first.return_value = None
    return mock_session


@pytest.fixture(scope='function')
def mock_session_query_delete_recipe(mock_deleted_recipe) -> MagicMock:
    session = MagicMock(spec=Session)
    mock_query = MagicMock()

    mock_recipe_record = create_autospec(RecipeRecord, instance=True, spec_set=True)

    mock_recipe_record.recipe_id = mock_deleted_recipe.recipe_id
    mock_recipe_record.title = mock_deleted_recipe.title
    mock_recipe_record.description = mock_deleted_recipe.description
    mock_recipe_record.ingredients = mock_deleted_recipe.ingredients
    mock_recipe_record.steps = mock_deleted_recipe.steps
    mock_recipe_record.image_url = mock_deleted_recipe.image_url
    mock_recipe_record.is_archived = mock_deleted_recipe.is_archived
    mock_recipe_record.created_at = mock_deleted_recipe.created_at
    mock_recipe_record.updated_at = mock_deleted_recipe.updated_at

    mock_query.filter_by().first.return_value = mock_recipe_record
    session.query.return_value = mock_query
    return session
