'''
Created on Aug 9, 2012

@author: PENNETTI
'''
'''
145 is a curious number, 
as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are 
equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums
they are not included.
'''
def factorial(n):
    try:
        int(n)
    except ValueError:
        return("Input must be a number.") 
    if n < 0:
        return("Input must be 0 or greater.")
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def sum_digits_factorial(n):
    try:
        int(n)
    except ValueError:
        return("Input must be a number.")
    sum = 0
    for c in range(len(str(n))):
        sum += factorial(int(str(n)[c]))
    if sum == n:
        return n
    else:
        return 0
    
def sum_factorions():
    sum = 0
    for n in range (3, 50000):
        sum += sum_digits_factorial(n)
    return sum
    
print(sum_factorions())