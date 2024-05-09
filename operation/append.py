from operation.operation import Operation

class Append(Operation):
    def get_name() -> str:
        return 'append'

    def check_arguments(args: list[any]) -> bool:
        return all([type(arg) == list for arg in args]) and len(args) > 0
    
    def evaluate(args: list) -> any:
        res = []
        for arg in args:
            res += arg
        return res