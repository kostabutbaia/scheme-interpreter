from procedure.procedure import Procedure

from operation.and_logic import And
from operation.or_logic import Or
from operation.equals_logic import Equals
from operation.is_null import IsNull
from operation.cond import Cond
from operation.product import Product
from operation.plus import Addition
from operation.minus import Subtraction
from operation.append import Append
from operation.car import Car
from operation.cdr import Cdr
from operation.cons import Cons
from operation.length import Length


from errors.unknown_operation import UnknownOperation
from errors.invalid_syntax import InvalidSyntax

from parser.utils import get_list_of_objects, string_to_list
from errors.wrong_arg_amount import WrongArgumentsAmount

from parser.function_parser import FunctionWrapper, Lambda, Eval, Apply

def string_to_procedure(line: str, definitions: dict[str, FunctionWrapper]) -> Procedure | list | str:
    stripped_line = line.strip()
    line_type = get_type(stripped_line)
    if line_type == Procedure:
        lst = get_list_of_objects(stripped_line)
        args = []

        # Condition logic
        if lst[0] == Cond.get_name():
            cond_args = lst[1:]
            for i, arg in enumerate(cond_args):
                cond_args_objects = get_list_of_objects(arg)
                if cond_args_objects[0] == 'else' and i != len(cond_args)-1:
                    raise InvalidSyntax()
                if cond_args_objects[0] == 'else' and i == len(cond_args)-1:
                    args.append(string_to_procedure(cond_args_objects[1], definitions))
                    break
                cond_value = string_to_procedure(cond_args_objects[0], definitions).eval()
                if cond_value == '#t':
                    args.append(string_to_procedure(cond_args_objects[1], definitions))
                    break
        else:
            for item in lst[1:]:
                args.append(string_to_procedure(item, definitions))
        return get_procedure(lst[0], args, definitions)
    elif line_type == list:
        res = string_to_list(stripped_line)
        return res
    elif line_type == Lambda:
        lst = get_list_of_objects(stripped_line)
        arguments_to_lambda = lst[1:]
        func = FunctionWrapper('lambda', Lambda.get_arg_names(lst[0]), Lambda.get_expression_string(lst[0]))
        return func_to_procedure(func, arguments_to_lambda, definitions)
    elif line_type == Eval:
        return string_to_procedure(Eval.get_expression_string(stripped_line), definitions)
    elif line_type == Apply:
        return string_to_procedure(Apply.get_expression_string(stripped_line), definitions)
    elif line_type == str:
        if stripped_line in definitions:
            return string_to_procedure(definitions[stripped_line].get_expression(), definitions)
        return stripped_line


def get_type(line: str) -> Procedure | list | str:
    if line[0] == "(" and line[-1] == ")":
        if line[1:-1].strip()[1:].strip()[:6] == 'lambda':
            return Lambda
        if line[1:-1].strip()[:6] == 'lambda':
            return str
        if line[1:-1].strip()[:4] == 'eval':
            return Eval
        if line[1:-1].strip()[:5] == 'apply':
            return Apply
        return Procedure
    if line[:2] == "'(" and line[-1] == ")":
        return list
    else:
        return str

def get_procedure(name: str, args: list[str], definitions: dict[str, FunctionWrapper]) -> Procedure:
    # built-in operations
    if name == Addition.get_name():
        return Procedure(Addition, args)
    elif name == Subtraction.get_name():
        return Procedure(Subtraction, args)
    elif name == Append.get_name():
        return Procedure(Append, args)
    elif name == Car.get_name():
        return Procedure(Car, args)
    elif name == Cdr.get_name():
        return Procedure(Cdr, args)
    elif name == Cons.get_name():
        return Procedure(Cons, args)
    elif name == And.get_name():
        return Procedure(And, args)
    elif name == Or.get_name():
        return Procedure(Or, args)
    elif name == Equals.get_name():
        return Procedure(Equals, args)
    elif name == Product.get_name():
        return Procedure(Product, args)
    elif name == Cond.get_name():
        return Procedure(Cond, args)
    elif name == IsNull.get_name():
        return Procedure(IsNull, args)
    elif name == Length.get_name():
        return Procedure(Length, args)
    
    # defined functions
    if name in definitions:
        return func_to_procedure(definitions[name], args, definitions)

    raise UnknownOperation(name)

    
def func_to_procedure(func_object: FunctionWrapper, args: list, definitions: dict[str, FunctionWrapper]) -> Procedure:
    expression = func_object.get_expression()
    arg_names = func_object.get_arg_names()
    func_name = func_object.get_name()

    if len(arg_names) != len(args):
        raise WrongArgumentsAmount(len(args), func_name)
    
    evaluated_args = []
    for arg in args:
        if type(arg) == str:
            evaluated_args.append(str(arg))
        if type(arg) == list:
            evaluated_args.append(f"'({' '.join(map(str, arg))})")
        if type(arg) == Procedure:
            res = arg.eval()
            if type(res) == str:
                evaluated_args.append(res)
            if type(res) == list:
                evaluated_args.append(f"'({' '.join(map(str, res))})")
    
    for i, arg_name in enumerate(arg_names):
        expression = expression.replace(f' {arg_name} ', f' {evaluated_args[i]} ')
        expression = expression.replace(f' {arg_name})', f' {evaluated_args[i]})')
        expression = expression.replace(f'({arg_name} ', f'({evaluated_args[i]} ')

    return string_to_procedure(expression, definitions)
