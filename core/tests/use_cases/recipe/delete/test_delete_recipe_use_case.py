from unittest.mock import patch

import pytest

from adapters.src.repositories import MemoryRecipeRepository
from core.src.exceptions import (
    RecipeBusinessException,
    RecipeNotFoundException,
    RecipeRepositoryException,
)
from core.src.use_cases import (
    CreateRecipe,
    CreateRecipeRequest,
    DeleteRecipe,
    DeleteRecipeRequest,
    DeleteRecipeResponse,
)


def test_delete_recipe_when_a_recipe_exists_should_return_true(
    recipe_repository: MemoryRecipeRepository,
    recipe_create_request: CreateRecipeRequest,
):
    create_recipe_use_case = CreateRecipe(recipe_repository)
    create_recipe_use_case(recipe_create_request)

    delete_recipe_use_case = DeleteRecipe(recipe_repository)
    request: DeleteRecipeRequest = DeleteRecipeRequest(recipe_id="recipe_1")
    response: DeleteRecipeResponse = delete_recipe_use_case(request=request)

    assert response is not None
    assert isinstance(response, DeleteRecipeResponse)
    assert response.is_archived is True


def test_delete_recipe_when_it_does_not_exist_should_raise_exception(
    recipe_repository: MemoryRecipeRepository,
):
    delete_recipe_use_case = DeleteRecipe(recipe_repository)
    request: DeleteRecipeRequest = DeleteRecipeRequest(recipe_id="recipe_1")

    with pytest.raises(RecipeNotFoundException):
        delete_recipe_use_case(request=request)


def test_delete_recipe_should_raise_exception_when_repository_fails(
    recipe_repository: MemoryRecipeRepository,
    recipe_create_request: CreateRecipeRequest,
):
    create_recipe_use_case = CreateRecipe(recipe_repository)
    create_recipe_use_case(recipe_create_request)
    delete_recipe_use_case = DeleteRecipe(recipe_repository)
    request: DeleteRecipeRequest = DeleteRecipeRequest(recipe_id="recipe_1")

    with patch.object(MemoryRecipeRepository, "delete", side_effect=RecipeRepositoryException("delete")):
        with pytest.raises(RecipeBusinessException):
            delete_recipe_use_case(request=request)
