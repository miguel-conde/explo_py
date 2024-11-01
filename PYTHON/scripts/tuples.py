# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 18:11:23 2021

Data Structures and Sequences

McKinney, Wes. Python for Data Analysis (p. 86). O'Reilly Media. Edición de Kindle. 

TUPLEs

@author: migue
"""

# A tuple is a fixed-length, immutable sequence of Python objects.

tup = 4,5,6
tup


nested_tup = (4,5,6), (7, 8)
nested_tup

# You can convert any sequence or iterator to a tuple by invoking tuple:
tuple([4,0,2])

tup = tuple('String')
tup

tup[0]

# While the objects stored in a tuple may be mutable themselves, once the tuple 
# is created it’s not possible to modify which object is stored in each slot:
    
tup = tuple([' foo', [1, 2], True])
tup[2] = False

# If an object inside a tuple is mutable, such as a list, you can modify it 
# in-place:
tup[1].append(3)
tup

# Concatenating tuples tuples
(4, None, 'foo') + (6, 0) + (' bar',)

(' foo', 'bar') * 4

# %% Unpacking tuples

tup = (4,5,6)

a, b, c = tup

tup = 4,5,(6,7)

a, b, (c, d) = tup

# Swap
a, b = 1, 2
b, a = a, b

# Iterating
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in seq:
    print("a = {}, b = {}, c={}".format(a, b, c))
    
# *rest
values = 1, 2, 3, 4, 5, 6

a, b, *rest = values
rest

# As a matter of convention, many Python programmers will use the underscore 
# (_) for unwanted variables:
a, b, *_ = values
_


# %% Tuple methods
a = (1, 2, 3, 2, 2, 4, 5, 1, 5)
a.count(2)
