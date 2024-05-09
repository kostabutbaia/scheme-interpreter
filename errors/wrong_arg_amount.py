class WrongArgumentsAmount(Exception):
    def __init__(self, amount: int, func_name: str):
        self.amount = amount
        self.func_name = func_name
    
    def __str__(self) -> str:
        return f'wrong amount {self.amount} of arguments passed to function "{self.name}"'