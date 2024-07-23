from unittest.mock import patch

from api.src.dtos import Recipe
from core.src.exceptions.business import BusinessException
from core.src.use_cases.recipe import CreateRecipe
from core.src.use_cases.recipe.create.response import CreateRecipeResponse


def test__create_recipe__when_it_is_called__then_it_should_return_recipe_and_status_code_200(
        create_recipe_response: Recipe, create_recipe_response_use_case: CreateRecipeResponse, client_session):

    with patch.object(CreateRecipe, "__call__", return_value=create_recipe_response_use_case):
        response = client_session.post("/recipes/", json=create_recipe_response)

    assert response.status_code == 200
    assert response.json() == create_recipe_response


def test__create_recipe__when_it_is_called__then_it_should_return_status_code_400_and_error_message(
        recipe_request_data: dict, client_session):
    error_message = "There was an error creating the recipe."

    with patch.object(CreateRecipe, "__call__", side_effect=BusinessException(error_message)):
        response = client_session.post("/recipes/", json=recipe_request_data)

    assert response.status_code == 400
    assert response.json() == {"detail": error_message}
