from unittest.mock import patch

from core.src.exceptions.business import BusinessException
from core.src.use_cases.recipe import ListRecipe, ListRecipeResponse


def test__list_all_recipes__when_there_are_no_recipes__then_it_should_return_empty_list_and_status_code_200(
        client_session):

    with patch.object(ListRecipe, "__call__", return_value=ListRecipeResponse(recipes=[])):
        response = client_session.get("/recipes/")

    assert response.status_code == 200
    assert len(response.json()) == 0


def test__list_all_recipes__when_it_is_called__then_it_should_return_recipes_and_status_code_200(
        list_recipes_response_use_case: ListRecipeResponse, list_recipes_response,
        client_session):

    with patch.object(ListRecipe, "__call__", return_value=list_recipes_response_use_case):
        response = client_session.get("/recipes/")

    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json() == list_recipes_response


def test__list_all_recipes__when_it_is_called__then_it_should_return_status_code_400_and_error_message(
        client_session):

    error_message = "There was an error listing the recipes."

    with patch.object(ListRecipe, "__call__", side_effect=BusinessException(error_message)):
        response = client_session.get("/recipes/")

    assert response.status_code == 400
    assert response.json() == {"detail": error_message}
