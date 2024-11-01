# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:21:44 2021

Data Structures and Sequences

McKinney, Wes. Python for Data Analysis (p. 86). O'Reilly Media. Edición de Kindle. 

LISTs

@author: migue
"""

# In contrast with tuples, lists are variable-length and their contents can 
# be modified in-place.
a_list = [2, 3, 7, None]

tup = 'foo', 'foo', 'bar'
b_list = list(tup)
b_list 

b_list[1] = 'abcde'
b_list

# Lists and tuples are semantically similar (though tuples cannot be modified) 
# and can be used interchangeably in many functions. The list function is 
# frequently used in data processing as a way to materialize an iterator or 
# generator expression:
gen = range(10)
gen
tuple(gen)
list(gen)

# %% Adding and removing elements

# %% APPEND
# Elements can be appended to the end of the list with the append method: 
b_list.append('dwarf') 
b_list 

# %% INSERT
# Using insert you can insert an element at a specific location in the list:
b_list.insert(1, 'red')
b_list 

## WARNING: insert is computationally expensive compared with append.

# %% POP
# The inverse operation to insert is pop, which removes and returns an element 
# at a particular index:
b_list.pop(2)
b_list

# %% REMOVE
# Elements can be removed by value with remove, which locates the first such 
# value and removes it from the list:
b_list.append('foo')
b_list
b_list.remove('foo')
b_list

# %% IN
# Check if a list contains or NOT a value using the in keyword:
'dwarf' in b_list

'dwarf' not in b_list

# %% Concatenating and combining lists

# %% + 
# Similar to tuples, adding two lists together with + concatenates them: 
[4, None, 'foo'] + [7, 8, (2, 3)] 

# %% EXTEND
# If you have a list already defined, you can append multiple elements to it 
# using the extend method: 
x = [4, None, 'foo'] 
x.extend([ 7, 8, (2, 3)])
x 

# %% Sorting
a = [7, 2, 5, 3, 1]
a.sort()
a

# %% SECONDARY SORT KEY
b = [' saw', 'small', 'He', 'foxes', 'six']
b.sort(key = len)
b

# %% Binary search and maintaining a sorted list

# BISECT
# The built-in bisect module implements binary search and insertion into a 
# sorted list. 
# - bisect.bisect finds the location where an element should be inserted to 
#   keep it sorted.
# - bisect.insort actually inserts the element into that location
import bisect

c = [1, 2, 2, 2, 3, 4, 7]

bisect.bisect(c, 2)
bisect.bisect(c, 5)

bisect.insort(c, 6)
c

## WARNING: The bisect module functions do not check whether the list is sorted

# %% Slicing

# starrt:stop
seq = [7, 2, 3, 7, 5, 6, 0, 1] 
seq[ 1: 5]

seq[3:4] = [6, 3]
print(seq)

# WARNING:
# While the element at the start index is included, the stop index is not 
# included, so that the number of elements in the result is stop - start.

# Either the start or stop can be omitted, in which case they default to the 
# start of the sequence and the end of the sequence, respectively: 
    
seq[: 5] 

seq[ 3:] 

# Negative indices slice the sequence relative to the end: 
seq[-4:] 

seq[-6:-2] 

# A step can also be used after a second colon to, say, take every other 
# element:
seq[::2]

# A clever use of this is to pass -1, which has the useful effect of reversing 
# a list or tuple: 
seq[::-1]


# %% Built-in Sequence Functions

# %% ENUMERATE

for i, v in enumerate(seq):
    print("i = {}, v = {}".format(i, v))

# %% SORTED
sorted(seq)

sorted("crazy horse")

# %% ZIP
# zip “pairs” up the elements of a number of lists, tuples, or other sequences 
# to create a list of tuples: 
seq1 = [' foo', 'bar', 'baz'] 
seq2 = [' one', 'two', 'three'] 

zipped = zip( seq1, seq2) 

list( zipped) 

# zip can take an arbitrary number of sequences, and the number of 
# elements it produces is determined by the shortest sequence: 
seq3 = [False, True] 

list( zip( seq1, seq2, seq3)) 

# A very common use of zip is simultaneously iterating over multiple 
# sequences, possibly also combined with enumerate: 
    
for i, (a, b) in enumerate( zip( seq1, seq2)):
    print('{ 0}: {1}, {2}'. format( i, a, b))

# Given a “zipped” sequence, zip can be applied in a clever way to 
# “unzip” the sequence. Another way to think about this is converting a list 
# of rows into a list of columns. The syntax, which looks a bit magical, is: 
pitchers = [(' Nolan', 'Ryan'), (' Roger', 'Clemens'), 
            (' Curt', 'Schilling')] 

first_names, last_names = zip(* pitchers) 

first_names 
last_names


# %% REVERSED
# reversed iterates over the elements of a sequence in reverse order:
list( reversed( range( 10)))
