# This program demonstrates the usage of copy module.

import copy

# Reference to the same list: 
spam = ['A','B','C','D']
reference = spam

reference[0] = 'Son Goku'

print(spam)      #['Son Goku','B','C','D']
print(reference) #['Son Goku','B','C','D']

# Reference to different list:

list = ['E','F','G','H']
list_copy = copy.copy(list)

list_copy[0] = 'Son Goku'

print(list)      #['E','F','G','H']
print(list_copy) #['Son Goku','F','G','H']
