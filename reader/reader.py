from parser.function_parser import FunctionWrapper, get_func_definitions, get_list_of_procedures

from parser.string_to_procedure import string_to_procedure

from procedure.procedure import Procedure

class FileReader:
    """
    Reads the script file with function definitions and commands

    Can execute the commands with exec method
    """
    def __init__(self, filepath: str):
        self.filepath = filepath
        with open(self.filepath, 'r') as f:
            script = f.read()
            if script != '':
                self.definitions: dict[str, FunctionWrapper] = get_func_definitions(script)
                procedures_strings: list[str] = get_list_of_procedures(script)

        self.procedures: list[Procedure] = [string_to_procedure(line, self.definitions) for line in procedures_strings]
    
    def exec(self) -> None:
        for procedure in self.procedures:
            result = procedure.eval()
            if type(result) == list:
                print(f"'({' '.join(result)})")
            else:
                print(result)