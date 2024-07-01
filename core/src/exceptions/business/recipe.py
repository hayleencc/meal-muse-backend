from .base import BusinessException, CreateException


class RecipeBusinessException(BusinessException):
    """Recipe business exception"""


class RecipeCreateException(CreateException):
    def __init__(self) -> None:
        super().__init__(entity_type="Recipe")
