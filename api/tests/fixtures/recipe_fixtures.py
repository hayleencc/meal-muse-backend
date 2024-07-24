import pytest

from api.src.dtos import Recipe
from core.src.use_cases.recipe import CreateRecipeResponse


@pytest.fixture
def recipe_request_data() -> dict:
    request = {
        "recipe_id": None,
        "title": "Recipe 1",
        "description": "Description 1",
        "ingredients": ["Ingredient 1", "Ingredient 2"],
        "steps": ["Step 1", "Step 2"],
        "image_url": "https:/mage.com/image.jpg",
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
    }
    return request


@pytest.fixture
def create_recipe_response() -> Recipe:
    return {
        "recipe_id": "f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f",
        "title": "Recipe 1",
        "description": "Description 1",
        "ingredients": ["Ingredient 1", "Ingredient 2"],
        "steps": ["Step 1", "Step 2"],
        "image_url": "https:/mage.com/image.jpg",
        "is_archived": False,
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
    }


@pytest.fixture
def create_recipe_response_use_case() -> CreateRecipeResponse:
    return CreateRecipeResponse(
        recipe_id="f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f",
        title="Recipe 1",
        description="Description 1",
        ingredients=["Ingredient 1", "Ingredient 2"],
        steps=["Step 1", "Step 2"],
        image_url="https:/mage.com/image.jpg",
        is_archived=False,
        created_at="2021-01-01T00:00:00",
        updated_at="2021-01-01T00:00:00",

    )
