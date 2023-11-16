(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  'YOUR-CODE-HERE
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
)


(define (unique s)
  'YOUR-CODE-HERE
)


(define (replicate x n)
    (define (replicate-tail x n accumulator)
    (if (= n 0)  
      accumulator                                        
      (replicate-tail x (- n 1) (cons x (accumulator)))))
  (replicate-tail x n nil)
  )


(define (accumulate combiner start n term)
  (if (zero? n)
    start
    (accumulate combiner (combiner start (term n)) (- n 1) term))
)


(define (accumulate-tail combiner start n term)
  (if (zero? n)
    start
    (accumulate-tail combiner (combiner start (term n)) (- n 1) term))
)


(define-macro (list-of map-expr for var in lst (variadic condition))
  (cond 
   ((null? condition)
     `(map (lambda (,var) ,map-expr) ,lst))
   ((and (equal? 'if (car condition)) (not (null? (cadr condition))))
     `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,(cadr condition)) ,lst))))
  ; (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))
)

(define-macro (for formal iterable body)
              (list 'map (list 'lambda (list formal) body) iterable))

(define (var x (variadic y))
  (if (null? y)
    (list x)
    (append y (list x))))
