from operation.operation import Operation

from functools import reduce

class Product(Operation):
    def get_name() -> str:
        return '*'

    def check_arguments(args: list[str]) -> bool:
        return all([arg.replace('-', '').isdigit() for arg in args]) and len(args) > 1
    
    def evaluate(args: list) -> str:
        return str(reduce(lambda x,y: x*y ,map(int, args)))