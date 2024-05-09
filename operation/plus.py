from operation.operation import Operation

class Addition(Operation):
    def get_name() -> str:
        return '+'

    def check_arguments(args: list[any]) -> bool:
        return all([arg.replace('-', '').isdigit() for arg in args]) and len(args) > 0
    
    def evaluate(args: list) -> str:
        return str(sum(map(int, args)))