from unittest.mock import patch

from api.src.dtos import RecipeDeleted
from core.src.exceptions.business import BusinessException
from core.src.use_cases import DeleteRecipe, DeleteRecipeResponse


def test__delete_recipe__when_it_is_called__then_it_should_return_recipe_is_archived_in_true(
        recipe_id: str, delete_recipe_response:
        RecipeDeleted, delete_recipe_use_case:
        DeleteRecipeResponse, client_session
):

    with patch.object(DeleteRecipe, "__call__", return_value=delete_recipe_use_case):
        response = client_session.delete(f"/recipes/{recipe_id}")

    assert response.status_code == 200
    assert response.json() == delete_recipe_response


def test__delete_recipe__when_it_is_called_and_business_exception_is_raised__then_it_should_return_status_code_400(
        recipe_id: str, client_session):

    with patch.object(DeleteRecipe, "__call__", side_effect=BusinessException()):
        response = client_session.delete(f"/recipes/{recipe_id}")

    assert response.status_code == 400
