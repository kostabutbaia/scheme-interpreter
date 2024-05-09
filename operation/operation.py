from abc import ABC, abstractclassmethod

class Operation(ABC):
    """
    Operation abstract class, it's implementations must implement two methods:
        - check_arguments, which checks if given arguments are valid for the evaluate method
        - evaluate, which evaluates the result given the arguments
    """

    @abstractclassmethod
    def get_name() -> str:
        """ Returns the name of this operation """
        pass

    @abstractclassmethod
    def check_arguments(args: list[any]) -> bool:
        """ Checks if given arguments satisfy this operation, arguments must be either int or list """
        pass

    @abstractclassmethod
    def evaluate(args: list[any]) -> any:
        """ Evaluates the operation with the given arguments """
        pass
