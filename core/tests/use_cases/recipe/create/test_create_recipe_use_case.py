from datetime import datetime

from adapters.src.repositories.memory import MemoryRecipeRepository
from core.src.use_cases.recipe import CreateRecipe, CreateRecipeRequest, CreateRecipeResponse


def test_create_recipe_should_return_a_recipe_create_is_succesfully():
    recipe_repository: MemoryRecipeRepository = MemoryRecipeRepository()
    create_recipe_use_case = CreateRecipe(recipe_repository)

    recipe_request = CreateRecipeRequest(
        recipe_id="recipe_1",
        title="recipe_title",
        description="recipe_description",
        ingredients=["ingredient_1", "ingredient_2"],
        steps=["step_1", "step_2"],
        image_url="http://image.com",
    )

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

    create_recipe_use_case(recipe_request)
    response = create_recipe_use_case(recipe_request)

    assert response == expected_response
