class InvalidArgsError(Exception):
    def __init__(self, operation: str, args: list[any]):
        self.args = args
        self.operation = operation
    
    def __str__(self) -> str:
        return f'invalid arguments for operation "{self.operation}": {self.args}'