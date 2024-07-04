from typing import List, Optional

from sqlalchemy.orm import Session

from core.src.exceptions import RecipeRepositoryException
from core.src.models import Recipe
from core.src.repository import RecipeRepository

from .tables import RecipeRecord


class SQLRecipeRepository(RecipeRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, recipe: Recipe) -> Optional[Recipe]:
        try:
            recipe_to_create = RecipeRecord(
                recipe_id=recipe.recipe_id,
                title=recipe.title,
                description=recipe.description,
                ingredients=recipe.ingredients,
                steps=recipe.steps,
                image_url=recipe.image_url
            )
            with self.session as session:
                session.add(recipe_to_create)
                session.flush()
                session.commit()
                sector_created_id = str(recipe_to_create.recipe_id)
            return Recipe(**{**recipe._asdict(), 'recipe_id': sector_created_id})
        except Exception:
            self.session.rollback()
            raise RecipeRepositoryException(method="create")

    def get_by_id(self, recipe_id: str) -> Optional[Recipe]:
        return None

    def edit(self, recipe: Recipe) -> Optional[Recipe]:
        return None

    def delete(self, recipe_id: str) -> Optional[Recipe]:
        return None

    def list_all(self) -> List[Recipe]:
        return []
