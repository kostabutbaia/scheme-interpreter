class UnbalancedBrackets(Exception):
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return f'Unbalanced brackets in the expression'