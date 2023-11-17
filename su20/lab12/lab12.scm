
(define-macro (def func args body)
  `(define ,(cons func args) ,body))


(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define all-three-multiples
  (map-stream (lambda (x) (+ x 3)) (cons-stream 0 all-three-multiples))
)

; atm.first = 0 + 3 ==> 3, atm.rest = atm (uncomputed)
; atm.rest.first = atm.first + 3 ==> 6, atm.rest = atm (uncomputed)


(define (compose-all funcs)
  (lambda (x) 
    (if (null? funcs) x ((compose-all (cdr funcs)) ((car funcs) x))))
)

(define (partial-sums stream)
  (define (helper init stream)
    ; a function that adds init to all the elements of stream
    (if (null? stream) nil
      (let ((to-add (+ init (car stream))))
        (cons-stream to-add (helper to-add (cdr-stream stream))))))
  (helper 0 stream)
)

; map x + 0 to stream(0, a1, a2, ...) => stream(0, a1, a2, ...)
; map x
