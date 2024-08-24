class BusinessException(Exception):
    pass


class AlreadyExistsException(BusinessException):
    def __init__(self, entity_type: str, entity_id: str):
        message = f"The {entity_type} with the id '{entity_id}' already exists."
        super().__init__(message)


class CreateException(BusinessException):
    def __init__(self, entity_type: str):
        message = f"An error occurred when creating the {entity_type} entity."
        super().__init__(message)


class NotFoundException(BusinessException):
    def __init__(self, entity_type: str, entity_id: str):
        message = f"The {entity_type} with the id '{entity_id}' does not exist."
        super().__init__(message)


class NoneException(BusinessException):
    def __init__(self, entity_type: str):
        message = f"The {entity_type} is None."
        super().__init__(message)


class NotDataException(BusinessException):
    def __init__(self, entity_type: str):
        message = f"The {entity_type} does not have data to update."
        super().__init__(message)
