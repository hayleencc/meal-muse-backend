from typing import List

from fastapi import APIRouter, HTTPException

from api.src.dtos import Recipe, RecipeDeleted
from core.src.exceptions.business import BusinessException
from core.src.use_cases import (
    CreateRecipe,
    CreateRecipeRequest,
    DeleteRecipe,
    DeleteRecipeRequest,
    EditRecipe,
    EditRecipeRequest,
    GetRecipeById,
    GetRecipeByIdRequest,
    ListRecipe,
)
from factories.use_cases import (
    create_recipe_use_case,
    delete_recipe_use_case,
    edit_recipe_use_case,
    get_recipe_by_id_use_case,
    list_recipes_use_case,
)

recipe_router = APIRouter(
    prefix="/recipes",
)


@recipe_router.post("/")
async def create_recipe(recipe: Recipe) -> Recipe:
    try:
        request = CreateRecipeRequest(
            title=recipe.title,
            description=recipe.description,
            ingredients=recipe.ingredients,
            steps=recipe.steps,
            image_url=recipe.image_url if recipe.image_url else None,
            created_at=recipe.created_at,
            updated_at=recipe.updated_at if recipe.updated_at else None,
        )
        create_use_case: CreateRecipe = create_recipe_use_case()
        response = create_use_case(request=request)
        return Recipe(**response._asdict())

    except BusinessException as e:
        raise HTTPException(status_code=400, detail=str(e))


@recipe_router.get("/")
async def get_recipes() -> List[Recipe]:
    try:
        list_use_case: ListRecipe = list_recipes_use_case()
        response = list_use_case()
        return [Recipe(**recipe._asdict()) for recipe in response.recipes] if response.recipes else []

    except BusinessException as e:
        raise HTTPException(status_code=400, detail=str(e))


@recipe_router.get("/{recipe_id}")
async def get_recipe_by_id(recipe_id: str) -> Recipe:
    try:
        use_case: GetRecipeById = get_recipe_by_id_use_case()
        request = GetRecipeByIdRequest(recipe_id=recipe_id)
        response = use_case(request=request)
        return Recipe(**response._asdict())

    except BusinessException as e:
        raise HTTPException(status_code=400, detail=str(e))


@recipe_router.patch("/")
async def edit_recipe(recipe: Recipe) -> Recipe:
    try:
        if not recipe.recipe_id:
            raise HTTPException(status_code=422, detail="recipe_id is required for editing a recipe")

        request = EditRecipeRequest(
            recipe_id=recipe.recipe_id,
            title=recipe.title,
            description=recipe.description,
            ingredients=recipe.ingredients,
            image_url=recipe.image_url,
        )
        edit_use_case: EditRecipe = edit_recipe_use_case()
        response = edit_use_case(request=request)
        return Recipe(**response._asdict())  # type: ignore

    except BusinessException as e:
        raise HTTPException(status_code=400, detail=str(e))


@recipe_router.delete("/{recipe_id}")
async def delete_recipe(recipe_id: str) -> RecipeDeleted:
    try:
        request = DeleteRecipeRequest(recipe_id=recipe_id)
        delete_use_case: DeleteRecipe = delete_recipe_use_case()
        response = delete_use_case(request=request)
        return RecipeDeleted(recipe_id=recipe_id, is_archived=response.is_archived)  # type: ignore

    except BusinessException as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
