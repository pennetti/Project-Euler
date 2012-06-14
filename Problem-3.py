'''
Created on May 13, 2012

@author: PENNETTI
'''
'''
Find the largest prime factor of 
a composite number.
(number provided)
'''

def largest_prime_factor(n):
    factors = []
    prime_factor = 2
    while prime_factor != n:
        if n % prime_factor == 0:
            factors.append(prime_factor)
            n /= prime_factor
            prime_factor = 2
        prime_factor += 1
    factors.append(prime_factor)
    return factors
    
    
def max(list):
    max = list[0]
    for i in range(0, len(list)):
        if (list[i] > max):
            max = list[i]
    return max

print(largest_prime_factor(600851475143))