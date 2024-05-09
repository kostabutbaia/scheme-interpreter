import unittest

from parser.string_to_procedure import *

class Test_GetListOfObjects(unittest.TestCase):

    def test_positive__get_list_of_objects(self):
        cases = [
            {'name': 'case 1','case': "(+ 1 2)", 'expected': ['+', '1', '2']},
            {'name': 'case 2','case': "(  +    1  2)", 'expected': ['+', '1', '2']},
            {'name': 'case 3','case': "(+ (+ 1 2) 2)", 'expected': ['+', '(+ 1 2)', '2']},
            {'name': 'case 4','case': "(+ (+ 1   2) 2)", 'expected': ['+', '(+ 1   2)', '2']},
            {'name': 'case 5','case': "(+ (+ 1   2) 2)", 'expected': ['+', '(+ 1   2)', '2']},
            {'name': 'case 6','case': "(+ (+ 1   (- 5 2)) 2)", 'expected': ['+', '(+ 1   (- 5 2))', '2']},
            {'name': 'case 7','case': "(+ (+  1    (- 5 2)) 2  2  4   (+ 1 2))", 'expected': ['+', '(+  1    (- 5 2))', '2', '2', '4', '(+ 1 2)']},
            {'name': 'case 9','case': "(a b c)", 'expected': ['a', 'b', 'c']},
            {'name': 'case 10','case': "(a)", 'expected': ['a']},
            {'name': 'case 11','case': "(a   )", 'expected': ['a']},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], get_list_of_objects(test_case['case']), msg=f"case: {test_case['name']}")
