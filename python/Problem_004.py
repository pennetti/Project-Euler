'''
Created on May 13, 2012

@author: PENNETTI
'''
'''
A palindromic number reads the same both 
ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 
91 99.

Find the largest palindrome made from the 
product of two 3-digit numbers.
'''
palindromes = []

#return true id number passed is palindrome
def is_palindrome(n):
    string = str(n)
    array = list(string)
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] == array[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

#return list of palindromes from 3-digit 
#factors
def product_palindromes():
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                palindromes.append(i * j)
                
def max(list):
    if len(list) == 0:
        return -1
    max = list[0]
    for i in range(0, len(list)):
        if (list[i] > max):
            max = list[i]
    return max
     
product_palindromes()
print(max(palindromes))