from operation.operation import Operation

class Cdr(Operation):
    def get_name() -> str:
        return 'cdr'

    def check_arguments(args: list[any]) -> bool:
        return len(args) == 1 and type(args[0]) == list
    
    def evaluate(args: list) -> any:
        return args[0][1:]