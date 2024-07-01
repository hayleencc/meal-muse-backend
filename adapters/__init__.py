import pytest

from adapters.src.repositories.memory import MemoryRecipeRepository


@pytest.fixture
def recipe_memory_repository() -> MemoryRecipeRepository:
    recipe_repository: MemoryRecipeRepository = MemoryRecipeRepository()
    return recipe_repository
