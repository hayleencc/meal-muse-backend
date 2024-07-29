from typing import List

from fastapi import APIRouter, HTTPException

from api.src.dtos import Recipe
from core.src.exceptions.business import BusinessException
from core.src.use_cases import CreateRecipe, CreateRecipeRequest, ListRecipe
from factories.use_cases import create_recipe_use_case, list_recipes_use_case

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
