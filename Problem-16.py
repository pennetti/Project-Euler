'''
Created on Jun 4, 2012

@author: PENNETTI
'''
'''
215 = 32768 and the sum of its digits 
is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the 
number 21000?
'''
num = 2 ** 1000
sum = 0

for i in range(0, len(str(num))):
    sum += int(str(num)[i])
    
print(sum)