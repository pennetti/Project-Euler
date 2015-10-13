'''
Created on Sep 1, 2012

@author: PENNETTI
'''
from decimal import getcontext
'''
A unit fraction contains 1 in the 
numerator. The decimal representation 
of the unit fractions with 
denominators 2 to 10 are given:

1/2    =     0.5
1/3    =     0.(3)
1/4    =     0.25
1/5    =     0.2
1/6    =     0.1(6)
1/7    =     0.(142857)
1/8    =     0.125
1/9    =     0.(1)
1/10    =     0.1

Where 0.1(6) means 0.166666..., and has
a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring 
cycle.

Find the value of d  1000 for which 1/d 
contains the longest recurring cycle in 
its decimal fraction part.
'''
from decimal import Decimal

# Set number of digits following decimal
# to 100
getcontext().prec = 1000



def primes(num):
    primes = [1] * num
    primes[0] = primes[1] = 0
    for i in range(2, num):
        if primes[i] == 1:
            for j in range(2, int(num / i)):
                primes[j * i] = 0
    return primes

def pattern_len(num):
    str = str(Decimal(1) / Decimal(num))
    pattern_len = 0
    patterns = []
    pat = ''
    for i in range(len(str)):
