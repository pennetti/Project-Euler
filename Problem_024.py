'''
Created on Sep 3, 2012

@author: PENNETTI
'''
'''
A permutation is an ordered arrangement
of objects. For example, 3124 is one 
possible permutation of the digits 1, 
2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, 
we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 
are:

012   021   102   120   201   210

What is the millionth lexicographic 
permutation of the digits 0, 1, 2, 3, 
4, 5, 6, 7, 8 and 9?
'''
'''
from math import factorial

def swap(term, index1, index2):
    term[index1], term[index2] = term[index2], term[index1]
    return term

def permute(term):
    term = list(term)
    perms = [str(term)]
    len_term = len(term)
    for _ in range(factorial(len_term)):
        for i in range(len_term - 1):
            perms.append(str(swap(term, i, i + 1)))
    return perms

print(sorted(permute('0123456789'))[999999])
'''
from itertools import permutations

print(sorted(permutations(range(10)))[999999])




