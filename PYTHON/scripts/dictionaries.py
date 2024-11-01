# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:47:48 2021

Data Structures and Sequences

McKinney, Wes. Python for Data Analysis (p. 86). O'Reilly Media. Edición de Kindle. 

Dictionaries

@author: migue
"""


# %% dict

# dict is likely the most important built-in Python data structure. A more 
# common name for it is hash map or associative array. It is a flexibly sized 
# collection of key-value pairs, where key and value are Python objects.

empty_dict = {} 

d1 = {' a' : 'some value', 'b' : [1,2, 3, 4]} 

d1

# You can access, insert, or set elements using the same syntax as for 
# accessing elements of a list or tuple: 
    
d1[ 7] = 'an integer' 

d1 

d1[' b'] 

# You can check if a dict contains a key using the same syntax used for 
# checking whether a list or tuple contains a value: 
    
'b' in d1 

# %% Deleting values: DEL, POP
# You can delete values either using the del keyword or the pop method (which
# simultaneously returns the value and deletes the key): 
    
d1[ 5] = 'some value' 
d1 

d1[' dummy'] = 'another value' 
d1 

del d1[ 5] 
d1

ret = d1. pop(' dummy') 
ret 
d1

# %% Iterators KEYS and VALUES
list(d1.keys())

# %% UPDATE
Y# ou can merge one dict into another using the update method:

d1. update({' b' : 'foo', 'c' : 12})
d1

# The update method changes dicts in-place, so any existing keys in the data 
# passed to update will have their old values discarded.

# %% Creating dicts from sequences

key_list = range(5)
value_list = reversed(range(5))
mapping = {} 

for key, value in zip( key_list, value_list): 
    mapping[ key] = value 
    
mapping
    
# Since a dict is essentially a collection of 2-tuples, the dict function 
# accepts a list of 2-tuples:

mapping = dict( zip( range( 5), reversed( range( 5))))

mapping

# %% Default values - GET, POP, SETDEFAULT

# The dict methods get and pop can take a default value to be returned:
mapping.get(0)
mapping.get(10, 'Not found')

# setdefault
words = [' apple', 'bat', 'bar', 'atom', 'book']

by_letter = {}

for word in words: 
    letter = word[ 0] 
    if letter not in by_letter: 
        by_letter[ letter] = [word] 
    else: 
        by_letter[ letter]. append( word)


by_letter = {}

for word in words: 
    letter = word[ 0] 
    by_letter.setdefault( letter, []). append( word)
    
# The built-in collections module has a useful class, defaultdict, which makes 
# this even easier. To create one, you pass a type or function for generating 
# the default value for each slot in the dict: 
  
from collections import defaultdict 

by_letter = defaultdict( list) 

for word in words: 
    by_letter[ word[ 0]]. append( word)



# %% Valid dict key types
# While the values of a dict can be any Python object, the keys generally have 
# to be immutable objects like scalar types (int, float, string) or tuples (all 
# the objects in the tuple need to be immutable, too). The technical term here 
# is hashability. You can check whether an object is hashable (can be used as a 
# key in a dict) with the hash function:
    
hash(' string')
hash(( 1, 2, (2, 3))) 
hash(( 1, 2, [2, 3])) # fails because lists are mutable
