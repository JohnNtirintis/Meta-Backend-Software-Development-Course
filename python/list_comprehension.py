#list comprehension syntax:
# [ <expression> for x in <sequence> if <condition>]

data = [2,3,5,7,11,13,17,19,23,29,31]

#Ex1: updating the same list
data = [x+3 for x in data]
print("Updating the list ", data)

#Ex1 but in a for loop:
#for x in range(len(data)):
#   data[x] = data[x] + 3

#Ex2: creating a different list with updated values
new_data = [x*2 for x in data]
print("Created new list: ", new_data)

#Ex3: if condition, multiples of four
fourx = [x for x in new_data if x % 4 == 0 ]
print("Divisble by 4: ", fourx)

#Ex4: update list with if condition
fourxsub = [x-1 for x in new_data if x % 4 == 0]
print("Divisble by 4 minus 1: ", fourxsub)

#Ex5: using range function
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)
