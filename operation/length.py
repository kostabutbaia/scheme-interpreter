from operation.operation import Operation

class Length(Operation):
    def get_name() -> str:
        return 'length'

    def check_arguments(args: list[any]) -> bool:
        return len(args) == 1 and type(args[0]) == list
    
    def evaluate(args: list) -> str:
        return str(len(args[0]))