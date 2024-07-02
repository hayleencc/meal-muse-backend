from unittest.mock import patch

import pytest

from adapters.src.repositories.memory import MemoryRecipeRepository
from core.src.exceptions import (
    RecipeBusinessException,
    RecipeNotFoundException,
    RecipeRepositoryException,
)
from core.src.use_cases import (
    CreateRecipe,
    CreateRecipeRequest,
    EditRecipe,
    EditRecipeRequest,
    EditRecipeResponse,
)


def test_edit_recipe_should_return_edited_recipe_when_recipe_exists(
    recipe_repository: MemoryRecipeRepository,
    recipe_create_request: CreateRecipeRequest,
    edit_recipe_response: EditRecipeResponse,
):
    create_recipe_use_case = CreateRecipe(recipe_repository)
    create_recipe_use_case(recipe_create_request)

    edit_recipe_use_case = EditRecipe(recipe_repository)
    request = EditRecipeRequest(
        recipe_id="recipe_1",
        title="New title",
        description="New description",
        ingredients=["New ingredient"],
        steps=["New step"],
        image_url="http://new_image.com",
        updated_at=None,
    )
    response = edit_recipe_use_case(request=request)

    assert response == edit_recipe_response


def test_edit_recipe_when_recipe_does_not_exist_should_raise_exception(
    recipe_repository: MemoryRecipeRepository,
):
    edit_recipe_use_case = EditRecipe(recipe_repository)
    request = EditRecipeRequest(
        recipe_id="recipe_1",
        title="New title",
        description="New description",
        ingredients=["New ingredient"],
        steps=["New step"],
        image_url="http://new_image.com",
        updated_at=None,
    )

    with pytest.raises(RecipeNotFoundException):
        edit_recipe_use_case(request=request)


def test_edit_recipe_should_raise_exception_when_repository_fails(
    recipe_repository: MemoryRecipeRepository,
    recipe_create_request: CreateRecipeRequest,
):
    create_recipe_use_case = CreateRecipe(recipe_repository)
    create_recipe_use_case(recipe_create_request)
    edit_recipe_use_case = EditRecipe(recipe_repository)
    request = EditRecipeRequest(
        recipe_id="recipe_1",
        title="New title",
        description="New description",
        ingredients=["New ingredient"],
        steps=["New step"],
        image_url="http://new_image.com",
        updated_at=None,
    )

    with patch.object(MemoryRecipeRepository, "edit", side_effect=RecipeRepositoryException("edit")):
        with pytest.raises(RecipeBusinessException):
            edit_recipe_use_case(request=request)
