from .base import BusinessException, CreateException, NotFoundException


class RecipeBusinessException(BusinessException):
    """Recipe business exception"""


class RecipeCreateException(CreateException):
    def __init__(self) -> None:
        super().__init__(entity_type="Recipe")


class RecipeNotFoundException(NotFoundException):
    def __init__(self, recipe_id: str) -> None:
        super().__init__(entity_type="Recipe", entity_id=recipe_id)


class RecipeNoneException(BusinessException):
    def __init__(self, entity_id: str) -> None:
        super().__init__(entity_type="Recipe", entity_id=entity_id)
