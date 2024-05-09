(and #f #f)
(and #t #t)
(or #t #f)

(or (or #f #f) (and #f #t) #f)

(cond ((and #t #t) first) ((or #f #f) 1) (else (+ 1 (+ 1 (+ 1 2)))))

(= 1 1)
(= 1 2)