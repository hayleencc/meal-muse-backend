import datetime

import pytest

from core.src.models import Recipe


@pytest.fixture
def mock_recipe() -> Recipe:
    return Recipe(
        recipe_id=1,
        title="Test Recipe",
        description="Test Description",
        ingredients=["ingredient1", "ingredient2"],
        steps=["step1", "step2"],
        image_url="https://test.com/test.jpg",
        is_archived=False,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
