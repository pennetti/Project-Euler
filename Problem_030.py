'''
Created on Sep 5, 2012

@author: PENNETTI
'''
'''
Surprisingly there are only three 
numbers that can be written as the sum 
of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not 
included.

The sum of these numbers is 1634 + 8208
 + 9474 = 19316.

Find the sum of all the numbers that 
can be written as the sum of fifth 
powers of their digits.
'''
# With 7 digit numbers, the highest 
# value is 413343, i.e. the highest sum 
# of the 5th powers of a 7 digit number 
# only adds up to a 6 digit number.  So 
# we only need to loop from 2 to 354294.
def is_five_narcissistic(n):
    _sum = 0
    n = str(n)
    for i in range(len(n)):
        _sum += int(n[i]) ** 5
    return int(n) == _sum

def sum_narcissistic():
    _sum = 0
    for i in range(2, 354294):
        if is_five_narcissistic(i):
            _sum += i
    return _sum

print(sum_narcissistic())