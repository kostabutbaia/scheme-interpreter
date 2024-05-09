# Scheme Interpreter
This is an interpreter for a scheme language, to run it you need python installed on your system. to run your scheme file you can use the following command:
```
python main.py <path_to_file>
```
where `<path_to_file>` is the path to the scheme `.scm` file

there are example scheme codes to run in `example/` directory, like:
```
python main.py example/recursion.scm
```

# Syntax
In the file you can define functions with `define` keyword or write procedures which will be executed and result will be displayed on the terminal

### Procedures

Procedure is an operation with it's arguments for the operation, an argument can be a procedure. for example a simple operation is the sum of numbers
```scm
(+ 1 2 3 4 5)
```
running the above command with this procedure in the file will print 15 to the terminal

### Functions

A function is defined with `define` keyword, when a function is defined in the file, it can be then used in procedures, for example:
```scm
(define (sum x y) (+ x y))

(sum 1 2)
```
In the procedure we've used the above defined function sum. you can run this with `python main.py example/simple_sum.py`

### Lambda functions
There are also anonymous lambda functions which are defined with `lambda` keyword.
for example we can execute a simple lambda function like:
```scm
((lambda (x y) (+ x y)) 1 2)
```
which will print 3 to the terminal. you can run this with `python main.py example/simple_lambda.py`

## Operations

There are built in simple operations in the interpeter which can be used on lists or strings

### Plus

Plus is simple arithmetic operation, which takes in only integers and returns their sum
```scm
(+ 1 1 1) -> returns 3
```

### Minus

Minus is simple arithmetic operation, which takes in only integers and returns first argument minus the rest
```scm
(- 10 1 1 1) -> returns 7
```

### Append

Append is an operation on lists, which takes in lists as argument and returns those lists concatenated
```scm
(append '(a 2) '(3 c) '(5 6)) -> returns '(a 2 3 c 5 6)
```

And other scheme operations like cond, car, cdr, or, and, product, equals and cond

## Map and Filter

In `example/recursion.scm` there are map and filter functions defined, you can run with command:
```
python main.py example/recursion.py
```



