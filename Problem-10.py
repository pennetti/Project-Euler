'''
Created on May 17, 2012

@author: PENNETTI
'''
'''
The sum of the primes below 10 is 
2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below 
two million.
'''


def sieve(n):
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for i in range(2, n):
        if primes[i] == True:
            j = 2
            while i * j < n:
                primes[i * j] = False
                j += 1
    return primes
                
def add_primes(n):
    primes_sum = 0
    _primes = sieve(n)
    for i in range(0, len(_primes)):
        if _primes[i]:
            primes_sum += i
    return primes_sum

print(add_primes(2000000))
                