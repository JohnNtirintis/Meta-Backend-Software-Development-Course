# Dictionary Comprehensions syntax:
# dict = { key:value for key, value in <sequence> if <condition> }

# Using range() function and no input list
usingRange = {x:x*2 for x in range(12+1)}
print("Using range(): ", usingRange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list ot create dict: ", numdict)

# Using two input lists
# The zip() function takes iterables (can be zero or more),
# aggregates them in a tuple, and returns it.
months_dict = {key:value for (key, value) in zip(number,months) }
print("Using two lists: ", months_dict)