; Group Members: Brad Stephens, John Murray
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
; Dependencies: mult_list (function)
; Returns: atom (number)
(defun add_list (lis)
    (cond   ((NULL lis) 0)
            ((LISTP (CAR lis)) (+ (mult_list (CAR lis)) (add_list (CDR lis)) ) )
            ((+ (CAR lis) (add_list (CDR lis) ) ))
    )
)


; Function: mult_list
; Purpose: used to multiply elements of a list together
;          calls add_list recursively
; Dependencies: add_list (function)
; Returns: atom (number)
(defun mult_list (lis)
    (cond   ((NULL lis) 1)
            ((LISTP (CAR lis) ) (* (add_list (CAR lis)) (mult_list(CDR lis)) ) )
            ((* (CAR lis) (mult_list (CDR lis) ) ) )
    )
)


; Function: calc_signal
; Purpose: used to calc signal (simple helper-function type abstraction, for
;               later modification without having to modify client code)
; Dependecies: add_list (function)
; Returns: atom (number)
(defun calc_signal (lis)
    (add_list lis)
)


; Function: is_prime_help
; Purpose: calculate if an atom is a prime number
;               helper function for is_prime
; Returns: T or NIL
(defun is_prime_help (divisor atm)
    (cond   ((= divisor atm) t)
            ((= (mod atm divisor) 0) nil)
            ((= 1 atm) t)
            ((is_prime_help (+ divisor 1) atm ) )
    )
)


; Function: is_prime
; Purpose: check if an atom is prime
; Dependencies: is_prime_help (function)
; Returns: T or NIL
(defun is_prime (atm)
    (is_prime_help 2 atm)
)


; Function: is_consecutive_prime
; Purpose: check if list given contains consecutive primes (from largest
;               to smallest - ex: 13, 11, 7)
; Returns: T or NIL
(defun is_consecutive_prime (lis)
    
    ;check for order (largest to smallest)
    ;and that they are all pries
    (setf temp -1)
    (dolist (atm lis)
        ;check thay they are in order
        (cond  ((= temp -1) (setf temp atm))
                   ((> temp atm) (setf temp atm))
                   ( (return-from is_consecutive_prime nil) )
        )
        
        ;check to make sure they are prime
        (if (EQ nil (is_prime atm)) (return-from is_consecutive_prime nil))
    )
    ;from here on out we can assume that they are in order and prime
    
    ;now make sure there are no prime numbers in between the items in the list
    (setf head (CDR lis))
    (setf next (CAR next))
    (dolist (atm lis)
        ;if next != nil
        (if (EQ (EQ next nil) nil)
            (setf temp atm)
            (loop while (> temp next) do
                (if (is_prime temp) (return-from is_consecutive_prime nil) )
                (setf temp (- temp 1))
            )
            (setf head (CDR head))
            (setf next (CAR head))
        )
    )
    
    ;if we have made it here, return true
    t
)


; Function: init
; Purpose: starting point for program
(defun init ()
    ;get input
    (print "Input correct sequence")
    (setf in (read))
    
    ;create list to contained calculated results
    (setf calc_list ())
    
    ;iterate through input, calculatig each one and populating 'calc_list'
    (dolist (lis in)
        (cons (calc_signal lis) calc_list)
    )
    
    ;we have calculated the list, now check to see if they are consecutive primes
    ;   note! - since the 'cons' function is ued, the list is in REVERSE order!
    (setf is_consec_primes (is_consecutive_prime calc_list))
    
    ;print out the results
)



; Start the program
(init)
; Give a message that the program is complete
"Done."