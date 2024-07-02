from datetime import datetime

import pytest

from adapters.src.repositories import MemoryRecipeRepository
from core.src.use_cases.recipe import (
    CreateRecipeRequest,
    CreateRecipeResponse,
    EditRecipeResponse,
    GetRecipeByIdResponse,
)


@pytest.fixture
def recipe_repository():
    return MemoryRecipeRepository()


@pytest.fixture
def recipe_create_request() -> CreateRecipeRequest:
    now = datetime.now()
    created_date = now.strftime("%d/%m/%Y %H:%M:%S")
    recipe_request = CreateRecipeRequest(
        recipe_id="recipe_1",
        title="recipe_title",
        description="recipe_description",
        ingredients=["ingredient_1", "ingredient_2"],
        steps=["step_1", "step_2"],
        image_url="http://image.com",
        is_archived=False,
        created_at=created_date,
        updated_at=created_date,
    )
    return recipe_request


@pytest.fixture
def recipe_create_response() -> CreateRecipeResponse:
    now = datetime.now()
    created_date = now.strftime("%d/%m/%Y %H:%M:%S")
    expected_response = CreateRecipeResponse(
        recipe_id="recipe_1",
        title="recipe_title",
        description="recipe_description",
        ingredients=["ingredient_1", "ingredient_2"],
        steps=["step_1", "step_2"],
        image_url="http://image.com",
        created_at=created_date,
        updated_at=created_date,
        is_archived=False,
    )
    return expected_response


@pytest.fixture
def get_recipe_by_id_response() -> GetRecipeByIdResponse:
    now = datetime.now()
    created_date = now.strftime("%d/%m/%Y %H:%M:%S")
    expected_response = GetRecipeByIdResponse(
        recipe_id="recipe_1",
        title="recipe_title",
        description="recipe_description",
        ingredients=["ingredient_1", "ingredient_2"],
        steps=["step_1", "step_2"],
        image_url="http://image.com",
        created_at=created_date,
        updated_at=created_date,
        is_archived=False,
    )
    return expected_response


@pytest.fixture
def edit_recipe_response() -> EditRecipeResponse:
    now = datetime.now()
    created_date = now.strftime("%d/%m/%Y %H:%M:%S")
    recipe_request = EditRecipeResponse(
        recipe_id="recipe_1",
        title="New title",
        description="New description",
        ingredients=["New ingredient"],
        steps=["New step"],
        image_url="http://new_image.com",
        is_archived=False,
        created_at=created_date,
        updated_at=None,
    )
    return recipe_request
