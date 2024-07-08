from abc import ABC, abstractmethod
from typing import List, Optional

from core.src.models import Recipe


class RecipeRepository(ABC):
    @abstractmethod
    def create(self, recipe: Recipe) -> Optional[Recipe]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, recipe_id: str) -> Optional[Recipe]:
        raise NotImplementedError

    @abstractmethod
    def edit(self, recipe: Recipe) -> Optional[Recipe]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, recipe_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[Recipe]:
        raise NotImplementedError
