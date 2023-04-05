menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# Map Example
# It returns a map object
map_coffee = map(find_coffee, menu)
print(map_coffee)
# I will print every coffee that starts with 'c'
# But ti will also print values of "None" if the coffee
# Doesnt start with 'c'
for x in map_coffee:
    print(x)


# Line to split the 2 outputs
print("=====================================================")

# Filter Example
# It returns a filter object
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
# It only returns the coffee that stars with 'c'
for x in filter_coffee:
    print(x)

