import os


class SQLConnection():
    def get_connection_string(self) -> str:
        connection = f"{os.environ.get('SQL_URL')}"
        return connection
