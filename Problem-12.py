'''
Created on May 19, 2012

@author: PENNETTI
'''
'''
The sequence of triangle numbers is generated 
by adding the natural numbers. So the 7th 
triangle number would be 
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten 
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven 
triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number 
to have over five divisors.

What is the value of the first triangle number 
to have over five hundred divisors?
'''
import math

def find_triangle_num():
    current_num = 1
    triangle_num = 1
    while num_divisors(triangle_num) <= 500:
        current_num += 1
        triangle_num += current_num
    return triangle_num

def num_divisors(n):
    num_divisors = 0
    divisor = 1
    while divisor <= int(math.sqrt(n)):
        if n % divisor == 0:
            num_divisors += 2
        divisor += 1
    return num_divisors

print(find_triangle_num())    
    
        
