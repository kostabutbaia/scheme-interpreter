from parser.utils import *

class FunctionWrapper:
    def __init__(self, func_name: str, arg_names: list[str], expression: str):
        self.arg_names = arg_names
        self.expression = expression
        self.func_name = func_name
    
    def __str__(self) -> str:
        return f"(func ({', '.join(self.arg_names)}) {self.expression})"
    
    def get_arg_names(self) -> list[str]:
        return self.arg_names
    
    def get_expression(self) -> str:
        return self.expression
    
    def get_name(self) -> str:
        return self.func_name
    
def get_func_definition(definition: str) -> FunctionWrapper:
    lst = get_list_of_objects(definition)
    if lst[1][1] != '(' and lst[1][-1] != ')':
        return FunctionWrapper(lst[1], None, lst[2])

    define = get_list_of_objects(lst[1])

    if lst[0] == 'define':
        return FunctionWrapper(define[0], define[1:], lst[2])
    return None

def get_func_definitions(script: str) -> dict[str, FunctionWrapper]:
    defined_functions: dict[str, FunctionWrapper] = {}
    for script_element in get_list_of_functions(script):
        definition = get_func_definition(script_element)
        if definition != None:
            defined_functions[definition.get_name()] = definition

    return defined_functions


def get_list_of_procedures(script: str) -> list[str]:
    script = script.replace('\n', ' ').replace('\t', ' ')
    return list(filter(lambda x: get_list_of_objects(x)[0] != 'define', get_list_of_objects(f'({script})')))

def get_list_of_functions(script: str) -> list[str]:
    script = script.replace('\n', ' ').replace('\t', ' ')
    return list(filter(lambda x: get_list_of_objects(x)[0] == 'define', get_list_of_objects(f'({script})')))


class Lambda:
    def get_arg_names(line: str) -> list[str]:
        lambda_objs = get_list_of_objects(line)
        arg_names = get_list_of_objects(lambda_objs[1])
        return arg_names

    def get_expression_string(line: str) -> str:
        lambda_objs = get_list_of_objects(line)
        expression = lambda_objs[2]
        return expression


class Eval:
    def get_expression_string(line: str) -> str:
        lst = get_list_of_objects(line)
        return lst[1][1:]

class Apply:
    def get_expression_string(line: str) -> str:
        lst = get_list_of_objects(line)
        procedure_list = [lst[1]] + string_to_list(lst[2])
        return f"({' '.join(procedure_list)})"