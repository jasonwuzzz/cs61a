(define (filter-lst fn lst)
  (cond 
    ((null? lst) nil)
    ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
    (else (filter-lst fn (cdr lst)))
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (interleave first second)
  (cond
    ((null? first) second)
    ((null? second) first)
    (else (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))))
  )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
  (cond
    ((= n 1) (combiner start (term n)))
    (else (combiner (term n) (accumulate combiner start (- n 1) term)))
  )
)


(define (no-repeats lst)
; Not using filter-lst:
  ; (define (twice x lst)
  ;   (cond
  ;     ((null? lst) #f)
  ;     ((= x (car lst)) #t)
  ;     (else (twice x (cdr lst)))))
  ; (cond
  ;   ((<= (length lst) 1) lst)
  ;   ((twice (car lst) (cdr lst)) (no-repeats (cdr lst)))
  ;   (else (cons (car lst) (no-repeats (cdr lst))))
  ; )
; Step1: get the first element of lst
; Step2: filter out all elements equal to the first element
; Step3: concatenate the first element and the filtered, no-repeated version of rest of lst.
  (define (helper x)
    ; filter out all (car lst) from lst
    (not (= x (car lst)))
  )
  (if (null? lst) '()
    (cons (car lst) (no-repeats (filter-lst helper lst))))
)

; (no-repeats '(5 4 5 4 2 2))
; (no-repeats '(4 5 4 2 2))
; (no-repeats '(5 4 2 2))
; (cons 5 (no-repeats '(4 2 2)))
; (cons 5 (cons 4 (no-repeats '(2 2))))
; (cons 5 (cons 4 (no-repeats '(2))))
; (cons 5 (cons 4 (cons 2 ((no-repeats '())))))
