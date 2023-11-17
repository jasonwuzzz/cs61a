(define (reverse lst)
  ; (1 2 3) => (3 2 1)
  ; (3 2) + (1)
  ; (append (reverse (cdr lst)) start)
  (define (reverse-tail lst start)
    (if (null? lst)
      start
      (reverse-tail (cdr lst) (cons (car lst) start))))
  (reverse-tail lst nil))

(define (insert n lst)
  (define (insert-tail n lst start)
    (if (or (null? lst) (<= n (car lst)))
       (append (reverse start) (cons n lst))
       (insert-tail n (cdr lst) (cons (car lst) start))))
  (insert-tail n lst nil))


(define-macro (or-macro expr1 expr2)
  `(let ((v1 ,expr1))
     (if v1 v1 ,expr2)))
; Step1: evaluate expr1 to get result v1 (don't evaluate expr2--short circuiting rules)
; Step2: if v1 is true, return v1
; Step3: else return the value of expr2

(define-macro (prune-expr expr)
; scm> (prune-expr (+ 10))
; 10
; scm> (prune-expr (+ 10 100))
; 10
; scm> (prune-expr (+ 10 100 1000)) ==> (+ 10 1000)
; 1010
; scm> (prune-expr (prune-expr (+ 10 100) 'garbage)) ==> (prune-expr (+ 10 100)) ==> (+ 10)
; 10

; (+ 1 3 5)
; (append '(+) '(1 3 5))
  (define (prune expr)
      (cond ((null? expr)
            nil)
            ((or (null? (cdr expr)) (null? (cdr (cdr expr))))
            (list (car expr)))
            (else (cons (car expr) (prune (cdr (cdr expr)))))))
  (append (list (car expr)) (prune (cdr expr))))


(define-macro (when condition exprs)
  ; `(if ,condition
  ;     ,(cons 'begin exprs)
  ;     'okay))
  (list 'if condition (cons 'begin exprs) ''okay))