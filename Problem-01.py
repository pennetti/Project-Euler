'''
Created on May 12, 2012

@author: PENNETTI
'''
'''
Problem 1: Add all the natural 
numbers below one thousand that 
are multiples of 3 or 5.
'''
sum = 0

for i in range(1000):
    if i % 5 == 0 or i % 3 == 0:
        sum += i
        
print(sum)
