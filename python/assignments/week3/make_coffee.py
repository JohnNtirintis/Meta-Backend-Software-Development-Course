"""
Exercise: Write a "Make a Coffee" script. 
Goal: Use many functions to get accustomed to them
"""

def make_coffee():
    dose = add_coffee()
    add_water(dose)
    add_sugar()
    ice = iced_coffe()
    stir_coffee(ice)
    pour_coffee()
    cream = ask_cream()
    add_cream(cream)

def add_coffee():
    flag = False
    dose = input("Would you like a single  or a double dose of coffee? ")

    while not flag:
        if dose.lower() == "single":
            flag = True
        elif dose.lower() == "double":
            flag = True
        else:
            dose = input("Please enter a correct value Single/Double: ")

    return dose

def add_water(dose):
    if dose.lower()== "single":
        print("Adding water for a single dose of coffee")
    else:
        print("Adding water for double dose of coffee")

def add_sugar():
    flag = False
    sugar =  input("How would you like your coffee? Choices are: No Sugar, Little, Medium, Sweet, Very Sweet. Please enter your input: ")

    while not flag:
        if sugar.lower() == "no sugar":
            flag = True
        elif sugar.lower() == "little":
            flag = True
        elif sugar.lower() == "medium":
            flag = True
        elif sugar.lower() == "sweet":
            flag = True
        elif sugar.lower() == "very sweet":
            flag = True
        else:
            sugar = input("Please enter a correct value: ")
    return print(f"The amount of sugar you want is {sugar}")

def iced_coffe():
    check = input("Would you like your coffee to be iced or not? Yes/No ")
    ice = False

    while not ice:
        if check.lower() == "yes":
            ice = True
        elif check.lower() == "no":
            break
        else:
            check = input("Please enter either Yes or No ")
    return ice

        
def stir_coffee(ice):
    if ice:
        print("Adding ice")
    else: 
        print("No ice")

def pour_coffee():
    print("Pouring your coffee to a cup!")

def ask_cream():
    check = input("Would you like some cream? Yes/No ")
    cream = False

    while not cream:
        if check.lower() == "yes":
            cream = True
        elif check.lower() == "no":
            break
        else:
            check = input("Please enter a correct valye Yes/No ")
    return cream


def add_cream(cream):
    if cream:
        print("Adding cream!")
    else:
        print("No cream it is then!")

def __main__():
    make_coffee()
    print("Your coffee is ready!")

__main__()