import pytest

from core.src.models import Recipe
from core.src.use_cases.recipe import (
    CreateRecipeResponse,
    DeleteRecipeResponse,
    EditRecipeResponse,
    GetRecipeByIdResponse,
    ListRecipeResponse,
)


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
def create_recipe_response():
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


@pytest.fixture
def list_recipes_response():
    return [
        {
            "recipe_id": str(recipe_id+1),
            "title": "Recipe " + str(recipe_id+1),
            "description": "Description",
            "ingredients": ["Ingredient 1", "Ingredient 2"],
            "steps": ["Step 1", "Step 2"],
            "image_url": "https:/mage.com/image.jpg",
            "is_archived": False,
            "created_at": "2021-01-01T00:00:00",
            "updated_at": "2021-01-01T00:00:00",
        } for recipe_id in range(3)
    ]


@pytest.fixture
def list_recipes_response_use_case() -> ListRecipeResponse:
    recipes = [
        Recipe(
            recipe_id=str(i+1),
            title="Recipe " + str(i+1),
            description="Description",
            ingredients=["Ingredient 1", "Ingredient 2"],
            steps=["Step 1", "Step 2"],
            image_url="https:/mage.com/image.jpg",
            is_archived=False,
            created_at="2021-01-01T00:00:00",
            updated_at="2021-01-01T00:00:00",
        ) for i in range(3)
    ]
    return ListRecipeResponse(recipes=recipes)


@pytest.fixture
def get_recipe_by_id_response_use_case() -> GetRecipeByIdResponse:
    return GetRecipeByIdResponse(
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


@pytest.fixture
def get_recipe_by_id_response():
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
def edit_recipe_response_use_case() -> EditRecipeResponse:
    return EditRecipeResponse(
        recipe_id="f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f",
        title="Recipe 1 Updated",
        description="Description 1 Updated",
        ingredients=["Ingredient 1", "Ingredient 2"],
        steps=["Step 1", "Step 2"],
        image_url="https:/mage.com/image.jpg",
        is_archived=False,
        created_at="2021-01-01T00:00:00",
        updated_at="2021-01-01T00:00:00",
    )


@pytest.fixture
def edit_recipe_response():
    return {
        "recipe_id": "f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f",
        "title": "Recipe 1 Updated",
        "description": "Description 1 Updated",
        "ingredients": ["Ingredient 1", "Ingredient 2"],
        "steps": ["Step 1", "Step 2"],
        "image_url": "https:/mage.com/image.jpg",
        "is_archived": False,
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
    }


@pytest.fixture
def delete_recipe_use_case():
    return DeleteRecipeResponse(is_archived=True)


@pytest.fixture
def delete_recipe_response():
    return {
        "is_archived": True,
        "recipe_id": "f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f",
    }


@pytest.fixture
def recipe_id():
    return "f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f"
