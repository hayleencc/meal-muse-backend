from unittest.mock import patch

import pytest

from adapters.src.repositories.memory import MemoryRecipeRepository
from core.src.exceptions import (
    RecipeBusinessException,
    RecipeNotFoundException,
    RecipeRepositoryException,
)
from core.src.use_cases.recipe import (
    CreateRecipe,
    CreateRecipeRequest,
    GetRecipeById,
    GetRecipeByIdRequest,
    GetRecipeByIdResponse,
)


def test_get_recipe_by_id_should_return_recipe_when_recipe_exists(
    recipe_repository: MemoryRecipeRepository,
    recipe_create_request: CreateRecipeRequest,
    get_recipe_by_id_response_core: GetRecipeByIdResponse,
):
    create_recipe_use_case = CreateRecipe(recipe_repository)
    create_recipe_use_case(recipe_create_request)

    get_recipe_by_id_use_case = GetRecipeById(recipe_repository)
    request = GetRecipeByIdRequest(recipe_id="recipe_1")
    response = get_recipe_by_id_use_case(request=request)

    assert response == get_recipe_by_id_response_core


def test_get_recipe_by_id_should_raise_exception_when_recipe_does_not_exist(
    recipe_repository: MemoryRecipeRepository,
):
    get_recipe_by_id_use_case = GetRecipeById(recipe_repository)
    request = GetRecipeByIdRequest(recipe_id="recipe_1")

    with pytest.raises(RecipeNotFoundException):
        get_recipe_by_id_use_case(request=request)


def test_get_recipe_by_id_should_raise_exception_when_repository_fails(
    recipe_repository: MemoryRecipeRepository,
):
    get_recipe_by_id_use_case = GetRecipeById(recipe_repository)
    request = GetRecipeByIdRequest(recipe_id="recipe_1")

    with patch.object(MemoryRecipeRepository, "get_by_id", side_effect=RecipeRepositoryException("get_by_id")):
        with pytest.raises(RecipeBusinessException):
            get_recipe_by_id_use_case(request=request)
