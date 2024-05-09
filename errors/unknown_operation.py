class UnknownOperation(Exception):
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self) -> str:
        return f'unknown opearation name "{self.name}"'