'''
Created on May 14, 2012

@author: PENNETTI
'''
'''
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
'''

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i < n:
        if n % i == 0 and n != i:
            return False
        i += 2
    return True

def find_nth_prime(n):
    primes = 0
    num = 2
    while primes != n:
        if is_prime(num):
            primes += 1
        if primes == n:
            return num
        num += 1
       
print(find_nth_prime(10001))