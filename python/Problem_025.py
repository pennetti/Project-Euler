'''
Created on Aug 9, 2012

@author: PENNETTI
'''
'''
The Fibonacci sequence is defined by 
the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and 
F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term 
to contain three digits.

What is the first term in the Fibonacci
sequence to contain 1000 digits?
'''
import math
#f(n) = Floor(phi^n / sqrt(5) + 1/2)
#phi = (1 + sqrt(5)) / 2
def fib_log(n):
    try:
        int(n)
    except ValueError:
        return "Parameter for function 'fib_log(n)' must be an integer."
    
    phi = (1 + math.sqrt(5)) / 2
    try:
        return math.floor(math.pow(phi, n) / math.sqrt(5) + 0.5)
    except OverflowError:
        return "Overflow error."

# Returns the nth term in the Fibonacci sequence
def fib(n):
    try:
        int(n)
    except ValueError:
        return "Parameter for function 'fib(n)' must be an integer."
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def thousand_digit_fib():
    for n in range(1000, 1000000):
        print(fib_log(n))
        if len(str(fib(n))) == 1000:
            return n

def thouasand_digit_fib_2():
    fib1 = 1
    fib2 = 1
    term = 2
    while len(str(fib2)) < 1000:
        temp = fib1
        fib1 = fib2
        fib2 = temp + fib2
        term += 1
    return term
        
print(thouasand_digit_fib_2())
        
        
        
        
        