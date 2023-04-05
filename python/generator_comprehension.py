"""
Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets.
They are also more memory efficient as compared to list comprehensions. 
"""

data = [2,3,5,7,11,13,17,19,23,29,31]

gen_obj = (x for x in data)
# Returns a generator object
print(gen_obj)
# Class: generator
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")