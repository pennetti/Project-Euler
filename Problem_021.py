'''
Created on Aug 10, 2012

@author: PENNETTI
'''
'''
Let d(n) be defined as the sum of 
proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, 
then a and b are an amicable pair and 
each of a and b are called amicable 
numbers.

For example, the proper divisors of 220 
are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The 
proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.

Evaluate the sum of all the amicable 
numbers under 10000.
'''
import math

def divisors(n):
    try:
        int(n)
    except ValueError:
        return "Value error."
    
    divisors = []
    if n <= 0:
        return "Value must be greater than zero." 
    for m in range(1, math.ceil(n/2) + 1):
        if n % m == 0:
            divisors.append(m)
    return divisors

def sum_of_divisors(n):
    try:
        int(n)
    except ValueError:
        return "Value error."
    
    if n <= 0:
        return "Value must greater than zero." 
    _divisors = divisors(n)
    sum_of_divisors = 0
    for m in range(len(_divisors)):
        sum_of_divisors += int(_divisors[m])
    return sum_of_divisors

def sum_amicable_pairs():
    sum_amicable_pairs = 0
    for m in range(2, 10000):
        n = sum_of_divisors(sum_of_divisors(m))
        if m == n and m != sum_of_divisors(m):
            print(m)
            sum_amicable_pairs += m
    return sum_amicable_pairs

print(sum_amicable_pairs())

        
    
    
    
    
    