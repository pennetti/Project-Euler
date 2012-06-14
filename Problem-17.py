'''
Created on Jun 4, 2012

@author: PENNETTI
'''
'''
If the numbers 1 to 5 are written out in 
words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters 
used in total.

If all the numbers from 1 to 1000 (one 
thousand) inclusive were written out in 
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For 
example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred 
and fifteen) contains 20 letters. The use 
of "and" when writing out numbers is in 
compliance with British usage.
'''
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
unique = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = [""] * 9
#subtract one from the length of 'ones' to exclude ""
for i in range(1, len(ones) - 1):
    hundreds[i] = ones[i] + "hundred"
thousands = ["onethousand"]
_and = "and"

def sum_ones():
    #numbers one to nine
    sum = 0
    for i in range(0, len(ones)):
        sum += len(ones[i])
    return sum
    
def sum_uni():
    #numbers ten to nineteen
    sum = 0
    for i in range(0, len(unique)):
        sum += len(unique[i])
    return sum

def sum_tens():
    #numbers twenty to ninety-nine
    sum = 0
    for i in range(0, len(tens)):
        for j in range(0, len(ones)):
            sum += len(tens[i]) + len(ones[j]) 
    return sum

def sum_hundreds():
    #numbers one hundred to nine hundred and ninety-nine
    sum = 0
    for i in range(0, len(hundreds)):
        sum += len(hundreds[i])
    for j in range(0, len(hundreds)):
        sum += len(hundreds[i]) * 9 + sum_ones() + len(_and) * 99 + sum_tens() + sum_uni()
    return sum
        
total = sum_ones() + sum_uni() + sum_tens() + sum_hundreds() + len(thousands[0])
print(total)



        
