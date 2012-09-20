'''
Created on Sep 5, 2012

@author: PENNETTI
'''
'''
Problem 31
'''
'''
import sys

currency = [1, 2, 5, 10, 20, 50, 100, 200]
 
def recursive_sum(currency, target, part, counter):
    s = sum(part)
    
    if s == target:
        counter += 1
    if s >= target:
        return
    
    for i in range(len(currency)):
        n = currency[i]
        remains = currency[i+1:]
        recursive_sum(remains, target, part + [n], counter)
        
    return counter
    
def main():
    
    part = []
    print(recursive_sum(currency, 200, part, 0))
    
    return 0
    
if __name__ == "__main__":
    sys.exit(main())
'''
'''
for each item in the currency array backwards
    sum = 0
    while sum < target and i > 0:
        add the item to a sum
        if sum == target:
            subtract value from sum
            counter += 1
            decrement i
        if sum > target:
            subtract the value from sum
            decremenet i (go to next element to see if it will complete the sum)   
            
'''
currency = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
counter = 0
for i in range(len(currency) - 1, -1, -1):
    s = 0
    j = i
    while s < target and j > 0:
        s += currency[j]
        if s == target:
            counter += 1
            s -= currency[j]
            j -= 1
        if s > target:
            s -= currency[j]
            j -= 1
            
print(counter)
    
    
    
    
    
    
    
    
    
    
    
    
    
    