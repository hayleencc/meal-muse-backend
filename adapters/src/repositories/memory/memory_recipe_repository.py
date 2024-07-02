from typing import List, Optional

from core.src.exceptions.repository.recipe import RecipeRepositoryException
from core.src.models.recipe import Recipe
from core.src.repository import RecipeRepository


class MemoryRecipeRepository(RecipeRepository):
    recipes: List[Recipe]

    def __init__(self) -> None:
        self.recipes = []

    def create(self, recipe: Recipe) -> Optional[Recipe]:
        try:
            self.recipes.append(recipe)
            return recipe
        except Exception:
            raise RecipeRepositoryException(method="create")

    def get_by_id(self, recipe_id: str) -> Optional[Recipe]:
        try:
            return next((recipe for recipe in self.recipes if recipe.recipe_id == recipe_id), None)
        except Exception:
            raise RecipeRepositoryException(method="get by id")

    def edit(self, recipe_to_edit: Recipe) -> Optional[Recipe]:
        try:
            for recipe in self.recipes:
                if recipe.id == recipe_to_edit.id:
                    self.recipes.remove(recipe)
                    self.recipes.append(recipe_to_edit)
                    return recipe_to_edit
            return None
        except Exception:
            raise RecipeRepositoryException(method="edit")

    def list_all(self) -> List[Recipe]:
        try:
            return self.recipes
        except Exception:
            raise RecipeRepositoryException(method="list")

    def delete(self, recipe_id: str) -> Optional[Recipe]:
        raise NotImplementedError
