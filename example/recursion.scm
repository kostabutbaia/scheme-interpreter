(power 2 2)
(fib 15)

(filter '(1 2 3 4) (lambda (x) (= x 2)))

(map '(1 2 3 4) (lambda (x) (+ x 2)))

(+ 1 pi)

(factorial 4)

(eval '(+ 1 (+ 1 2)))

(apply * '(1 2 3))

(define pi (+ 4 2))

(define (power a b)
    (cond 
        ((= b 0) 1)
        (else (* a (power a (- b 1))))
    )
)

(define (fib n)
    (cond 
        ((= n 1) 1)
        ((= n 2) 1)
        (else (+ (fib (- n 1)) (fib (- n 2))))
    )
)

(define (filter lst func)
    (cond
        ((null? lst) '())
        ((func (car lst)) (cons (car lst) (filter (cdr lst) func)))
        (else (filter (cdr lst) func))
    )
)

(define (map lst func)
    (cond
        ((null? lst) '())
        (else (cons (func (car lst)) (map (cdr lst) func)))
    )
)

(define (factorial x)
        (cond ((= x 1) 1)
        (else (* x (factorial (- x 1))))
))