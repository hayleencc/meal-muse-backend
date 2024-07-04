from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session


@pytest.fixture
def mock_session() -> MagicMock:
    return MagicMock(spec=Session)


@pytest.fixture
def mock_session_exception() -> MagicMock:
    mock = MagicMock(spec=Session)
    mock.commit.side_effect = Exception
    return mock
