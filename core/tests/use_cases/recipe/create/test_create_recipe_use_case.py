from unittest.mock import patch

import pytest

from adapters.src.repositories.memory import MemoryRecipeRepository
from core.src.exceptions import (
    RecipeBusinessException,
    RecipeCreateException,
    RecipeRepositoryException,
)
from core.src.use_cases.recipe import CreateRecipe, CreateRecipeRequest, CreateRecipeResponse


def test_create_recipe_should_return_a_recipe_when_create_is_succesfully(
    recipe_create_request: CreateRecipeRequest,
    recipe_create_response: CreateRecipeResponse,
):
    recipe_repository: MemoryRecipeRepository = MemoryRecipeRepository()
    create_recipe_use_case = CreateRecipe(recipe_repository)

    create_recipe_use_case(recipe_create_request)
    response = create_recipe_use_case(recipe_create_request)

    assert response == recipe_create_response


def test_create_recipe_should_raise_exception_when_creation_fails(
    recipe_create_request: CreateRecipeRequest,
):
    recipe_repository: MemoryRecipeRepository = MemoryRecipeRepository()
    create_recipe_use_case = CreateRecipe(recipe_repository)

    with patch.object(MemoryRecipeRepository, "create", return_value=None):
        with pytest.raises(RecipeCreateException):
            create_recipe_use_case(recipe_create_request)


def test_create_recipe_should_raise_exception_when_repository_fails(
    recipe_create_request: CreateRecipeRequest,
):
    recipe_repository: MemoryRecipeRepository = MemoryRecipeRepository()
    create_recipe_use_case = CreateRecipe(recipe_repository)

    with patch.object(MemoryRecipeRepository, "create", side_effect=RecipeRepositoryException("create")):
        with pytest.raises(RecipeBusinessException):
            create_recipe_use_case(recipe_create_request)
