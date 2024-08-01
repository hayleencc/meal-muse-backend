from unittest.mock import patch

from core.src.exceptions import RecipeNotFoundException
from core.src.exceptions.business import BusinessException
from core.src.use_cases.recipe import GetRecipeById, GetRecipeByIdResponse


def test__get_recipe_by_id__when_it_is_called__then_it_should_return_recipe_and_status_code_200(
        get_recipe_by_id_response_use_case: GetRecipeByIdResponse, get_recipe_by_id_response,
        client_session):

    with patch.object(GetRecipeById, "__call__", return_value=get_recipe_by_id_response_use_case):
        response = client_session.get("/recipes/f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f")

    assert response.status_code == 200
    assert response.json() == get_recipe_by_id_response


def test__get_recipe_by_id__when_it_is_called__then_it_should_return_status_code_400_and_error_message(
        client_session):

    error_message = "There was an error getting the recipe."

    with patch.object(GetRecipeById, "__call__", side_effect=BusinessException(error_message)):
        response = client_session.get("/recipes/f7e0d1e1-6b5d-4f0a-9e9b-1a3b1e7b8f0f")

    assert response.status_code == 400
    assert response.json() == {"detail": error_message}


def test__get_recipe_by_id__when_recipe_id_doesnt_exist__then_it_should_return_status_code_400_and_error_message(
        client_session):

    error_message = "The Recipe with the id '1' does not exist."

    with patch.object(GetRecipeById, "__call__", side_effect=RecipeNotFoundException(recipe_id="1")):
        response = client_session.get("/recipes/1/")

    assert response.status_code == 400
    assert response.json() == {"detail": error_message}
