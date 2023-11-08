(define (factorial x)
		(if (= x 1)
		  	1
			(* x (factorial (- x 1)))
		)
	)


(define (fib n)
  (cond
    ((= n 0) 0)
    ((= n 1) 1)
    (else (+ (fib (- n 1)) (fib (- n 2))))
  )
)


(define (my-append a b)
  	(if (null? a) b
	(cons (car a) (my-append (cdr a) b))
        )
	)

(define (duplicate lst)
  	(if (null? lst) lst
	 (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
  	)
	)


(define (insert element lst index)
		(cond
		  ((null? lst) (list element))
		  ((> index (length lst)) "Index exceeded length" )
		  ((= index 0) (cons element lst))
		  (else (cons (car lst) (insert element (cdr lst) (- index 1))))
		)
	)

; scm> (define lst '(2 3 4))
; scm> (insert 1 lst 0)
; (1 2 3 4)
