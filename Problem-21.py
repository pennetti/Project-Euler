'''
Created on Jul 12, 2012

@author: PENNETTI
'''
'''
Using names.txt (right click and 'Save 
Link/Target As...'), a 46K text file 
containing over five-thousand first 
names, begin by sorting it into 
alphabetical order. Then working out 
the alphabetical value for each name, 
multiply this value by its alphabetical 
position in the list to obtain a name 
score.

For example, when the list is sorted 
into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 
938th name in the list. So, COLIN would 
obtain a score of 938  53 = 49714.

What is the total of all the name scores 
in the file?
'''


names_file = open('names.txt', 'r')
names_string = names_file.read().split(',');

def name_val(name):
    val = 0
    # Ignore the quotations
    for i in range(1, len(name) - 1):
        val += (ord(name[i]) - 64)
    return val

def names_sum(names):
    sum = 0
    for i in range(len(names)):
        sum += ((i + 1) * (name_val(names[i])))
    return sum

print(names_sum(sorted(names_string)))