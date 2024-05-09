from operation.operation import Operation

# from parser.string_to_procedure import string_to_procedure
from parser.utils import get_list_of_objects

class Cond(Operation):
    def get_name() -> str:
        return 'cond'

    def check_arguments(args: list[str]) -> bool:
        return len(args) == 1
    
    def evaluate(args: list) -> str:
        return args[0]