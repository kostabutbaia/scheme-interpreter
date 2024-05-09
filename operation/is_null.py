from operation.operation import Operation

class IsNull(Operation):
    def get_name() -> str:
        return 'null?'

    def check_arguments(args: list[str]) -> bool:
        return len(args) == 1 and type(args[0]) == list
    
    def evaluate(args: list) -> str:
        return '#t' if len(args[0]) == 0 else '#f'