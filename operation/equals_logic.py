from operation.operation import Operation

class Equals(Operation):
    def get_name() -> str:
        return '='

    def check_arguments(args: list[str]) -> bool:
        return all([arg.replace('-', '').isdigit() for arg in args]) and len(args) == 2
    
    def evaluate(args: list) -> str:
        return '#t' if args[0] == args[1] else '#f'