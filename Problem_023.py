'''
Created on Aug 9, 2012

@author: PENNETTI
'''
'''
A perfect number is a number for which 
the sum of its proper divisors is 
exactly equal to the number. For 
example, the sum of the proper divisors 
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the 
sum of its proper divisors is less than 
n and it is called abundant if this sum 
exceeds n.

As 12 is the smallest abundant number, 
1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of 
two abundant numbers is 24. By 
mathematical analysis, it can be shown 
that all integers greater than 28123 can 
be written as the sum of two abundant 
numbers. However, this upper limit cannot 
be reduced any further by analysis even 
though it is known that the greatest number 
that cannot be expressed as the sum of two 
abundant numbers is less than this limit.

Find the sum of all the positive integers 
which cannot be written as the sum of two 
abundant numbers.
'''
from math import sqrt

def sum_divisors(n):    
    # 1 is a factor common to all numbers
    sum = 1
    sqrt_n = sqrt(n)
    for m in range(2, int(sqrt_n) + 1):
        if n % m == 0:
            # Add the divisor and it's compliment
            sum += (m + n / m)
    if sqrt_n == int(sqrt_n):
        # Remove duplicate swaure factors
        sum -= sqrt_n
    return sum


# Range of numbers from 24-20162
def abundant_sums():
    sum_nonabundant_sums = 0
    abundants = set()
    for i in range(1, 20162):
        if sum_divisors(i) > i:
            abundants.add(i)
        # If a number minus an abundant number is not an
        # abundant number, then it cannot be expressed as the 
        # sum of two abundant numbers
        if not any( ((i - a) in abundants) for a in abundants):
            sum_nonabundant_sums += i
    return sum_nonabundant_sums

print(abundant_sums())




