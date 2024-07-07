from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session


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
