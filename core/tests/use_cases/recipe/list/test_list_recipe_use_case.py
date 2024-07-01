from unittest.mock import patch

import pytest

from adapters.src.repositories import MemoryRecipeRepository
from core.src.exceptions import RecipeBusinessException, RecipeRepositoryException
from core.src.use_cases.recipe import (
    CreateRecipe,
    CreateRecipeRequest,
    CreateRecipeResponse,
    ListRecipe,
    ListRecipeResponse,
)


def test_list_recipe_should_return_a_list_of_recipes(
    recipe_create_request: CreateRecipeRequest,
    recipe_create_response: CreateRecipeResponse,
):
    recipe_repository: MemoryRecipeRepository = MemoryRecipeRepository()
    create_recipe_use_case = CreateRecipe(recipe_repository)
    create_recipe_use_case(recipe_create_request)

    list_recipe_use_case = ListRecipe(recipe_repository)
    response = list_recipe_use_case()

    assert len(response) > 0
    assert isinstance(response, ListRecipeResponse)


def test_list_recipe_should_raise_exception_when_repository_fails(
    recipe_create_request: CreateRecipeRequest,
):
    recipe_repository: MemoryRecipeRepository = MemoryRecipeRepository()
    create_recipe_use_case = CreateRecipe(recipe_repository)
    create_recipe_use_case(recipe_create_request)

    list_recipe_use_case = ListRecipe(recipe_repository)

    with patch.object(MemoryRecipeRepository, "list_all", side_effect=RecipeRepositoryException("list_all")):
        with pytest.raises(RecipeBusinessException):
            list_recipe_use_case()
