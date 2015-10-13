'''
Created on Sep 14, 2012

@author: Travis Pennetti

Given a target string, and a list of 
string fragments, write a function that
returns true or false if any number of 
fragments can be combined to form the 
target string.

target: "abcd"
frags:"a", "9", "cd", "b"
returns: true.

Order of the fragments doesn't matter, 
each fragment can only be used once. 
'''
def frag(target, frags):
    removed = []
    original = target
    for i in range(len(frags)):
        if frags[i] in target:
            target = target.replace(frags[i], "", 1)
            removed.append(frags[i])
        if len(removed) != 0:
            for j in range(len(removed)):
                if removed[j] in frags[i] and\
                not (removed[j] is frags[i]) and frags[i] in original:
                    frags[i] = frags[i].replace(removed[j], "", 1)
                    target = target.replace(frags[i], "", 1)
    return target is None or len(target) == 0

'''Test Case 1'''
target = "abcd"
frags = ["a", "9", "cd", "b"]

print(frag(target, frags))

'''Test Case 2'''
target = "abcd"
frags = ["a", "ab", "d", "2", "cd" ]

print(frag(target, frags))

'''Test Case 3'''
target = "abcd"
frags = ["a", "ba", "d", "2", "cd" ]

print(frag(target, frags))