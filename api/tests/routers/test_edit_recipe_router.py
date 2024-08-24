from unittest.mock import patch

from api.src.dtos import Recipe
from core.src.exceptions.business import BusinessException
from core.src.use_cases.recipe import EditRecipe, EditRecipeResponse


def test__edit_recipe__when_it_is_called__then_it_should_return_recipe_and_status_code_200(
        edit_recipe_response: Recipe, edit_recipe_response_use_case: EditRecipeResponse, client_session):

    with patch.object(EditRecipe, "__call__", return_value=edit_recipe_response_use_case):
        response = client_session.patch("/recipes/", json=edit_recipe_response)

    assert response.status_code == 200
    assert response.json() == edit_recipe_response


def test__edit_recipe__when_it_is_called_and_business_exception_is_raised__then_it_should_return_status_code_400(
        edit_recipe_response: Recipe, client_session):

    with patch.object(EditRecipe, "__call__", side_effect=BusinessException()):
        response = client_session.patch("/recipes/", json=edit_recipe_response)

    assert response.status_code == 400
