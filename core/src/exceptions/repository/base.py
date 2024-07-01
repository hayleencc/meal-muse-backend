class RepositoryException(Exception):
    def __init__(self, entity_type: str, method: str):
        message = f"Something was wrong trying to {method} the {entity_type}"
        super().__init__(message)
