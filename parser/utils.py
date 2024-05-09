from errors.unbalanced_brackets import UnbalancedBrackets
from errors.invalid_syntax import InvalidSyntax

def string_to_list(line: str) -> list:
    """ 
    This method takes a list string like '(1 2 3) and returns python list ['1', '2', '3']
    """
    line = line[2:-1]
    return [i for i in filter(lambda x: x != '', line.split(' '))]


def get_list_of_objects(line: str) -> list[str]:
    """ 
    This method accepts a string of a procedure "(<item1> <item2> <item3> ...)"
    and it returns a list of strings [<item1>, <item2>, <item3>, ...]
    """
    line = line.replace('\n', ' ')
    if len(line) < 3 or line[0] != '(' or line[-1] != ')':
        raise InvalidSyntax(line)
    line = line[1:-1]
    line = line.strip()
    objects = []
    cur_object = ''

    bracket_counter = 0
    for c in line:
        if c == ' ' and bracket_counter == 0:
            objects.append(cur_object)
            cur_object = ''
            continue
        if c == '(':
            bracket_counter += 1
        if c == ')':
            bracket_counter -= 1
            if bracket_counter == 0:
                cur_object += c
                objects.append(cur_object)
                cur_object = ''
                continue

        cur_object += c
    if bracket_counter != 0:
        raise UnbalancedBrackets
    objects.append(cur_object)
    return list(filter(lambda x: x != '', objects))