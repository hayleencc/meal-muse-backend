from datetime import datetime

import pytest

from core.src.use_cases.recipe import CreateRecipeRequest, CreateRecipeResponse


@pytest.fixture
def recipe_create_request() -> CreateRecipeRequest:
    recipe_request = CreateRecipeRequest(
        recipe_id="recipe_1",
        title="recipe_title",
        description="recipe_description",
        ingredients=["ingredient_1", "ingredient_2"],
        steps=["step_1", "step_2"],
        image_url="http://image.com",
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
    )
    return expected_response
