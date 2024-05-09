from operation.operation import Operation

class Cons(Operation):
    def get_name() -> str:
        return 'cons'

    def check_arguments(args: list[str]) -> bool:
        return len(args) == 2 and type(args[0]) == str and type(args[1]) == list
    
    def evaluate(args: list) -> list:
        return list(args[0]) + args[1]