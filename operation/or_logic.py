from operation.operation import Operation

class Or(Operation):
    def get_name() -> str:
        return 'or'

    def check_arguments(args: list[str]) -> bool:
        return all([arg == '#t' or arg == '#f' for arg in args]) and len(args) > 0
    
    def evaluate(args: list) -> str:
        return '#t' if any([arg == '#t' for arg in args]) else '#f'