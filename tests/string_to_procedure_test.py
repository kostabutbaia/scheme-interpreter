import unittest

from parser.string_to_procedure import *

from parser.function_parser import FunctionWrapper

class Test_StringToProcedure(unittest.TestCase):

    """
     Operation Tests

     Tests Involving built-in operations
    """

    def test_plus__string_to_procedure(self):
        cases = [
            {'name': 'case 1','case': "(+ 1 2)", 'expected': '3'},
            {'name': 'case 2','case': "(  +    1  2)", 'expected':'3'},
            {'name': 'case 3','case': "(+ (+ 1 2) 2)", 'expected': '5'},
            {'name': 'case 4','case': "(+ (+ 1   2) 2)", 'expected': '5'},
            {'name': 'case 5','case': "(+ (+ 1   2) 2)", 'expected': '5'},
            {'name': 'case 6','case': "(+ (+ 1   (- 5 1)) 2)", 'expected': '7'},
            {'name': 'case 7','case': "(+ (+  1    (- 5 2)) 2  2  4   (+ 1 2))", 'expected': '15'},
            {'name': 'case 8','case': "(- 2 1)", 'expected': '1'},
            {'name': 'case 9','case': "(- 1 2)", 'expected': '-1'},
            {'name': 'case 10','case': "(- 1 (- 1 3))", 'expected': '3'},
            {'name': 'case 11','case': "(- 1 (- 1 (- 1 (- 1 3))) 2)", 'expected': '1'},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], string_to_procedure(test_case['case'], dict()).eval(), msg=test_case['name'])

    def test_append__string_to_procedure(self):
        cases = [
            {'name': 'case 1','case': "(append '(1 2 3) '(1 2 3))", 'expected': ['1', '2', '3', '1', '2', '3']},
            {'name': 'case 2','case': " (  append   '(1 2 3)   '(1 2 3 3))", 'expected': ['1', '2', '3', '1', '2', '3', '3']},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], string_to_procedure(test_case['case'], dict()).eval(), msg=test_case['name'])

    
    def test_car__string_to_procedure(self):
        cases = [
            {'name': 'case 1','case': "(car '(1 2 3))", 'expected': '1'},
            {'name': 'case 2','case': "(car '(4))", 'expected': '4'},
            {'name': 'case 3','case': "(car  '(  6  2 3 1 2  3))", 'expected': '6'},
            {'name': 'case 4','case': "(car  '(  2))", 'expected': '2'},
            {'name': 'case 5','case': "(car  '(  a))", 'expected': 'a'},
            {'name': 'case 5','case': " ( car  '(  a b c d))", 'expected': 'a'},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], string_to_procedure(test_case['case'], dict()).eval(), msg=test_case['name'])

    def test_cdr__string_to_procedure(self):
        cases = [
            {'name': 'case 1','case': "(cdr '(1 2 3))", 'expected': ['2', '3']},
            {'name': 'case 2','case': "(cdr '(1))", 'expected': []},
            {'name': 'case 3','case': "(cdr '())", 'expected': []},
            {'name': 'case 4','case': "(cdr '( 1 43 5 6 2))", 'expected': ['43', '5', '6', '2']},
            {'name': 'case 5','case': "(append (cdr '( 1 43 5 6 2)) '(1 1 1))", 'expected': ['43', '5', '6', '2', '1', '1', '1']},
            {'name': 'case 6','case': "(append (cdr (append '(1 2) '(3 4))) '(1 1 1))", 'expected': ['2', '3', '4', '1', '1', '1']},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], string_to_procedure(test_case['case'], dict()).eval(), msg=test_case['name'])

    def test_cons__string_to_procedure(self):
        cases = [
            {'name': 'case 1','case': "(cons a '(a b c))", 'expected': ['a', 'a', 'b', 'c']},
            {'name': 'case 1','case': "(cons a '())", 'expected': ['a']},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], string_to_procedure(test_case['case'], dict()).eval(), msg=test_case['name'])

    """ 
     Tests With Functions

     Tests involving user defined functions with is passed to the string_to_procedure function
    """
    def test_positive4__string_to_procedure(self):
        cases = [
            {
                'name': 'case 1', 
                'case': "(my_append '(1 2 3) '(1 2 3))",
                'expected': ['1', '2', '3', '1', '2', '3'],
                'funcs': {"my_append": FunctionWrapper("my_append", ['x', 'y'], '(append x y)')}
            },
            {
                'name': 'case 2', 
                'case': "  ( myappend1  '(  1 2 3) '(1 2  3) )",
                'expected': ['1', '2', '3', '1', '2', '3'],
                'funcs': {"myappend1": FunctionWrapper("myappend1", ['x', 'y'], '(myappend2 x y)'), "myappend2": FunctionWrapper("myappend2", ['x', 'y'], '(append x y)')}
            },
            {
                'name': 'case 3', 
                'case': "  ( myappend1  '(  1 2 3) (myappend1 '(1 2 3) '(5 5 5)) )",
                'expected': ['1', '2', '3', '1', '2', '3', '5', '5', '5'],
                'funcs': {"myappend1": FunctionWrapper("myappend1", ['x', 'y'], '(myappend2 x y)'), "myappend2": FunctionWrapper("myappend2", ['x', 'y'], '(append x y)')}
            },
            {
                'name': 'case 4', 
                'case': "  ( second_elem  '(1 2 3))",
                'expected': '2',
                'funcs': {"second_elem": FunctionWrapper("second_elem", ['lst'], '(car (cdr lst))')}
            },
            {
                'name': 'case 5', 
                'case': "  ( second_elem  '(1 2 3))",
                'expected': '2',
                'funcs': {"second_elem": FunctionWrapper("second_elem", ['lst'], '(car (my_cdr lst))'), "my_cdr": FunctionWrapper("my_cdr", ['lst'], '(cdr lst)')}
            },
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], string_to_procedure(test_case['case'], test_case['funcs']).eval(), msg=test_case['name'])

    def test_lambda__string_to_procedure(self):
        cases = [
            {'name': 'case 1','case': "(  (    lambda (x y) (+ x y)) 1 2)", 'expected': '3'},
            {'name': 'case 2','case': "(  (    lambda (x   y) ( append   x  y)) '(1) '(2))", 'expected': ['1', '2']},
            {'name': 'case 3','case': "(append (  (    lambda (x   y) ( append   x  y)) '(1) '(2)) '(1))", 'expected': ['1', '2', '1']},
            {'name': 'case 4','case': "(append (  (    lambda (x   y z) ( append   x  y z)) '(1) '(2) '(1 2 3)) '(1))", 'expected': ['1', '2', '1', '2', '3', '1']},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], string_to_procedure(test_case['case'], dict()).eval(), msg=test_case['name'])
