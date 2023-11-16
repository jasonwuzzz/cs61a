; Use a Scheme list to represent infinite sequence.
(define (naturals n)
  (cons n (naturals (+ n 1))))

; CONS is a regular procedure
; both its operands must be evalued before Pair is constructed

(define (naturals n)
  (cons-stream n (naturals (+ n 1))))

(define nat (naturals 0))

; the first element is evaluated explicitly
; the rest of stream are computed only when needed (lazy evaluation)

; (cons-stream <operand1> <operand2>)
; <operand1> ==> evaluate and store its value as the first part of Pair.
; <operand2> ==> construct a Promise and stores it as the second part of Pair. ==`cdr-stream`==> evaluate the rest of stream and stores it (only evaluated once without recomputing it).

; Question 1.1
(define (has-even? s)
  (cond ((null? s) #f)
        ((even? (car s)) #t)
        (else (has-even? (cdr-stream s)))))

; Question 1.2
; Correct
(define (filter-stream f s) 
  (cond
    ((null? s) nil)
    ((f (car s)) (cons-stream (car s) (filter-stream f (cdr-stream s)))) 
    (else (filter-stream f (cdr-stream s)))))

; Incorrect
; (define (filter-stream f s)
;   (if (null? s) nil
;     (let ((rest (filter-stream f (cdr-stream s))))
;       (if (f (car s))
;         (cons-stream (car s) rest)
;         rest))))
; the rest gets evaluated before, which voilating the rule of lazy computation of STREAM.

; Question 1.3
(define (map-stream f s)
  (if (null? s)
    nil
    (cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

; Question 1.4
(define (slice s start end)
  (cond
    ((and (null? s) (> end start))
     "Index out of range.")
    ((> start end)
     "Invalid range.")
    ((not (zero? start))
     (slice (cdr-stream s) (- start 1) (- end 1)))
    ((not (zero? end))
     (cons (car s) (slice (cdr-stream s) start (- end 1))))
    (else nil)))

; Question 1.5
(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
    nil
    (cons-stream 
      (f (car xs) (car ys))
      (combine-with f (cdr-stream xs) (cdr-stream ys)))))

(define evens (combine-with + nat nat))

; (1 1 1 2  6  24 120  720) (cons-stream 1 factorials)
; (1 1 2 3  4   5   6    7) (cons-stream 1 (cdr-stream nat))
; (1 1 2 6 24 120 720 5040)
(define factorials (combine-with * (cons-stream 1 factorials) 
(cons-stream 1 (cdr-stream nat))))

; (0 0 0 1 1 2 3  5  8 13): (0 0) (fibs)
; (0 1 1 1 2 3 5  8 13 21): (0 1) (cdr-stream fibs)
; (0 1 1 2 3 5 8 13 21 34)
(define fibs (combine-with + (cons-stream 0 (cons-stream 0 fibs)) (cons-stream 0 (cons-stream 1 (cdr-stream fibs)))))

; (0   1    1+x    1+x+x^2)     (cons-stream 0 pantion)
; (x^0 x^1   x^2       x^3)     poly
; (1 1+x 1+x+x^2 1+x+x^2+x^3)
(define (poly x) 
  (cons-stream 1 (map-stream (lambda (ele) (* x ele)) (poly x))))

(define (term x)
  (combine-with / (poly x) factorials))

(define (exp x)
  (combine-with + (cons-stream 0 (exp x)) (term x)))

; Question 1.6
(define (sieve s)
  (if (null? s)
    nil
    (cons-stream (car s)
                 (sieve (filter-stream 
                   (lambda (x) (not (zero? (modulo x (car s))))) 
                   (cdr-stream s))))))

(define primes
  (sieve (naturals 2)))

; Question 2.1
(define-macro (make-lambda expr)
              `(lambda () ,expr))

; Question 2.2
; Use make-lambda to wrap (thunk) the expr in the second stream.
(define-macro (make-stream first second)
              `(cons ,first
                     (cons
                       (make-lambda ,(car (cdr second)))
                       nil)))

; Calling the lambda function to unwrap the expr.
(define (cdr-stream stream)
  ((car (cdr stream))))
