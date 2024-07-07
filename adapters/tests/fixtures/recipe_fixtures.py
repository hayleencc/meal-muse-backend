from datetime import datetime, timedelta

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
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )


@pytest.fixture
def mock_updated_recipe() -> Recipe:
    current_datetime = datetime.now()
    return Recipe(
        recipe_id=1,
        title="Test Recipe Updated",
        description="Test Description Updated",
        ingredients=["ingredient1 Updated", "ingredient2 Updated"],
        steps=["step1 Updated", "step2 Updated"],
        image_url="https://test.com/test_updated.jpg",
        is_archived=False,
        created_at=current_datetime - timedelta(days=1),
        updated_at=current_datetime,
    )
