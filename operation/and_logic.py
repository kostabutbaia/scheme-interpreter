from operation.operation import Operation

class And(Operation):
    def get_name() -> str:
        return 'and'

    def check_arguments(args: list[str]) -> bool:
        return all([arg == '#t' or arg == '#f' for arg in args]) and len(args) > 0
    
    def evaluate(args: list) -> str:
        return '#t' if all([arg == '#t' for arg in args]) else '#f'