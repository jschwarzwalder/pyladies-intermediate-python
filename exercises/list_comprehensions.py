import pytest

# Replace each "pass" statement with your code.

# Exercise 1
# Use list comprehension to create a function that multiplies
# each element in a sequence of numbers by 2
# ================================
def double(sequence):
    result = [ item*2 for item in sequence if item != 0 ]
    return result
        

def test_double():
    assert double(range(3)) == [0,2,4]

#print double([1,2,3,4])

# Exercise 2
# Use list comprehension to create a function that finds
# the odd elements in a sequence of numbers
# ================================
def odd(sequence):
    result = [item for item in sequence if item%2 != 0]
    return result

def test_odd():
    assert odd(range(6)) == [1,3,5]

#print odd(range(6))


# Exercise 3
# Use list comprehension to create a function that finds
# the elements divisible by 3 and 5 in a sequence of numbers
# ================================
def by_five(sequence):
    result = [ item for item in sequence if item%5 == 0 and item %3 ==0]
    return result
        

def test_by_five():
    assert by_five(range(1,31)) == [15, 30]
    
#print by_five(range(1,31))

# Exercise 4
# Use list comprehension to create a function that finds
# words containing the letter 'e' in a list of words
# ================================
def e_present(words):
	pass

def test_e_present():
	assert e_present(['dog', 'cat', 'heron', 'turtle', 'aardvark', 'pythons', 'elephant']) == ['heron', 'turtle', 'elephant']


# Exercise 5
# Use list comprehension to display the index position in front of each element
# of a list. For example, say you're given the list ["zero", "one", "two"]. 
# The output of your list comprehension would be ['0: zero', '1: one', '2: two']
# 
# Hint 1: use helper functions
# Hint 2: write a function that accepts the index position and element of each item
# in the list, and formats the element into the form 'index: element'
# Hint 3: use enumerate() in the iterator portion of the list comprehension
# ================================

def format_pair(sequence):
	pass

def test_format_pair():
	assert format_pair(["zero", "one", "two"]) == ['0: zero', '1: one', '2: two']
