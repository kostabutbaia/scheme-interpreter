class InvalidSyntax(Exception):
    def __init__(self, line: str):
        self.line = line
    
    def __str__(self) -> str:
        return f'invalid syntax: {self.line}'