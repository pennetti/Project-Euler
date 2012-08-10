'''
Created on May 13, 2012

@author: PENNETTI
'''
'''The sum of the squares of the first 
ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten 
natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of 
the squares of the first ten natural 
numbers and the square of the sum is 
3025  385 = 2640.

Find the difference between the sum of 
the squares of the first one hundred 
natural numbers and the square of the sum.
'''
import math

sum_of_squares = 0
square_of_sums = 0

for i in range (1,101):
    sum_of_squares += math.pow(i, 2)
    square_of_sums += i 
    
square_of_sums = math.pow(square_of_sums, 2)

print(square_of_sums - sum_of_squares)
