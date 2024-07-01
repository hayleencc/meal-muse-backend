from .base import RepositoryException


class RecipeRepositoryException(RepositoryException):
    def __init__(self, method: str):
        super().__init__(entity_type="Recipe", method=method)
