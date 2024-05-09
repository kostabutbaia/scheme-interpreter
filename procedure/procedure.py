from operation.operation import Operation
from errors.invalid_args import InvalidArgsError

class Procedure:
    """ 
    Procedure class encapsulares operation with it's arguments,
    it has a method eval which evaluates the operation on the arguments
    arguments can be either list, int or another Procedure.

    calling eval evaluates the Procedures in arguments first and then passes
    it the the operation's evaluate method

    if operation receives invalid arguments, eval method 
    will raise an InvalidArgsError Exception
    """
    def __init__(self, operation: Operation, args: list):
        self.operation: Operation = operation
        self.arguments: list[Procedure | str | list] = args

    def eval(self) -> str | list:
        """ 
        This method return the result of the procedure, which will be either list
        of strings or a string

        Calling eval evaluates the Procedures in arguments first and then passes
        it in the operation's evaluate method
        """
        args = []
        for object in self.arguments:
            if type(object) == list or type(object) == str:
                args.append(object)
            else:
                args.append(object.eval())
        if self.operation.check_arguments(args):
            return self.operation.evaluate(args)
        
        raise InvalidArgsError(self.operation.get_name(), args)