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
            self.session.add(recipe_to_create)
            self.session.flush()
            self.session.commit()
            recipe_created_id = str(recipe_to_create.recipe_id)
            return Recipe(**{**recipe._asdict(), 'recipe_id': recipe_created_id})
        except Exception:
            self.session.rollback()
            raise RecipeRepositoryException(method="create")

    def get_by_id(self, recipe_id: str) -> Optional[Recipe]:
        try:
            recipe_found = self.session.query(RecipeRecord).filter(RecipeRecord.recipe_id == recipe_id).first()
            if recipe_found is not None:
                return Recipe(
                    recipe_id=str(recipe_found.recipe_id),
                    title=str(recipe_found.title),
                    description=str(recipe_found.description),
                    ingredients=list(recipe_found.ingredients) if recipe_found.ingredients else [],
                    steps=list(recipe_found.steps) if recipe_found.steps else [],
                    image_url=str(recipe_found.image_url),
                    is_archived=bool(recipe_found.is_archived),
                    created_at=recipe_found.created_at,  # type: ignore
                    updated_at=recipe_found.updated_at  # type: ignore
                )
            return None
        except Exception:
            self.session.rollback()
            raise RecipeRepositoryException(method="get_by_id")

    def edit(self, recipe: Recipe) -> Optional[Recipe]:
        return None

    def delete(self, recipe_id: str) -> Optional[Recipe]:
        return None

    def list_all(self) -> List[Recipe]:
        try:
            records = (self.session.query(RecipeRecord).filter(RecipeRecord.is_archived.is_(False)).all())
            recipes_found = [Recipe(
                recipe_id=str(record.recipe_id),
                title=str(record.title),
                description=str(record.description),
                ingredients=list(record.ingredients) if record.ingredients else [],
                steps=list(record.steps) if record.steps else [],
                image_url=str(record.image_url),
                is_archived=bool(record.is_archived),
                created_at=record.created_at,  # type: ignore
                updated_at=record.updated_at  # type: ignore
            ) for record in records] if records else []
            return recipes_found
        except Exception:
            self.session.rollback()
            raise RecipeRepositoryException(method="list_all")
