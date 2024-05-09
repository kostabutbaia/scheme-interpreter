from operation.operation import Operation

class Car(Operation):
    def get_name() -> str:
        return 'car'

    def check_arguments(args: list[any]) -> bool:
        return len(args) == 1 and type(args[0]) == list and len(args[0]) > 0
    
    def evaluate(args: list) -> any:
        return args[0][0]