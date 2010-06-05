; Group Members: Brad Stephens, John Murray, ??Heyna Shaw??
; File Name: assignment_1.lisp
; Language Used: Common Lisp
; Description of Program:
;       
;       Takes an input of a list of lists and calculates
;       elements in the list to either be prime or non-
;       prime. If all numbers are prime, then it caclulates
;       to see if the numbers are consecutive primes

; Function: add_list
; Purpose: used to add elements of a list together
;          calls mult_list recursively
(defun add_list (lis)
    (cond   ((NULL lis) 0)
            ((LISTP (CAR lis)) (+ (mult_list (CAR lis)) (add_list (CDR lis)) ) )
            ((+ (CAR lis) (add_list (CDR lis) ) ))
    )
)

; Function: mult_list
; Purpose: used to multiply elements of a list together
;          calls add_list recursively
(defun mult_list (lis)
    (cond   ((NULL lis) 1)
            ((LISTP (CAR lis) ) (* (add_list (CAR lis)) (mult_list(CDR lis)) ) )
            ((* (CAR lis) (mult_list (CDR lis) ) ) )
    )
)

; Function: is_prime_help
; Purpose: calculate if an atom is a prime number
;          helper function for is_prime
(defun is_prime_help (divisor atm)
    (cond   ((= divisor atm) t)
            ((= (mod atm divisor) 0) nil)
            ((= 1 atm) t)
            ((is_prime_help (+ divisor 1) atm ) )
    )
)

; Function: is_prime
; Purpose: check if an atom is prime
(defun is_prime (atm)
    (is_prime_help 2 atm)
)

; Function: calc_signal
; Purpose: used to calc signal and determine primeness
(defun calc_signal (lis)
    (add_list lis)
)


; Function: init
; Purpose: starting point for program
(defun init ()
    ;get input
    (print "Input correct sequence")
    (setf in (read))
    
    ;create calculated list
    (setf cacl_list ())
    ;iterate through input
    (do (lis in)
        (add_list lis)
    )
)



; Start the program
(init)
; Give a message that the program is complete
"Done."