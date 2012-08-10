'''
Created on Jul 12, 2012

@author: PENNETTI
'''
'''
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 
= 3628800,
and the sum of the digits in the number 
10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 
100!
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_digits(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum

print(sum_digits(factorial(100)))