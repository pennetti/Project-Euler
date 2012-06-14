'''
Created on May 17, 2012

@author: PENNETTI
'''
'''
Created on May 16, 2012

@author: PENNETTI
'''
'''
A Pythagorean triplet is a set of three 
natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean 
triplet for which a + b + c = 1000.
Find the product abc.
'''
def brute_force():
    for i in range(0, 500):
        for j in range(0, 500):
            for k in range(0, 500):
                if (i**2 + j**2) - k**2 == 0 and i + j + k == 1000:
                    print(i * j * k)
                    
brute_force()