from operation.operation import Operation

class Subtraction(Operation):
    def get_name() -> str:
        return '-'

    def check_arguments(args: list[str]) -> bool:
        return all([arg.replace('-', '').isdigit() for arg in args]) and len(args) > 0
    
    def evaluate(args: list) -> str:
        return str(int(args[0]) - sum(map(int, args[1:])))