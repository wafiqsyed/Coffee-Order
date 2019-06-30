##
# My name is Wafiq Syed Rahmathulla and my student number is 250868594. I'm in Computer science 1026 in
# Professor Bauer's section
# This program computes the total price (in dollars) of either coffee or tea for various sizes and flavors.
#
## CONSTANTS ##
SMALL_PRICE = 1.50  #Price of small sized beverage.
MEDIUM_PRICE = 2.50 #Price of medium sized beverage.
LARGE_PRICE = 3.25 #Price of large sized beverage.
VANILLA_PRICE = 0.25 #Price of vanilla flavoring.
CHOCOLATE_PRICE = 0.75 #Price of chocolate flavoring.
MAPLE_PRICE = 0.50 #Price of maple flavoring.
LEMON_PRICE = 0.25 #Price of lemon flavoring.
MINT_PRICE = 0.50 #Price of mint flavoring.
costSize = 0.00  #Defining variables
costFlavoring = 0.00
size = "s"
flavoring = "none"
name = input("Please type your first name (no spaces): ").capitalize()  #Asks for person's name.
if name != name.strip():
    print("Please do not include space(s) in your name.")
    quit()
drink = input("Would you like coffee or tea (Answer c for coffee or t for tea)? ").lower()  #Finding out which type of drink is desired.
if drink == "t" or drink == "tea":
    drink = "tea"
if drink == "c" or drink == "coffee":
    drink = "coffee"
if drink == "t" or drink == "tea" or drink == "c" or drink == "coffee":  #Limiting input to acceptable forms.
    size = input("Please choose a size (small, medium, or large): ").lower()  #Size of drink, making sure the required inputs work
    if size == "small" or size == "s":
        costSize = SMALL_PRICE  #costs
        size = "small"
    elif size == "medium" or size == "m":
        costSize = MEDIUM_PRICE
        size = "medium"
    elif size == "large" or size == "l":
        costSize = LARGE_PRICE
        size = "large"
    else:
        print("Sorry, we don't have that size.")
        quit()
    if drink == "coffee":
        flavoring = input("Please choose from one of the following flavor options: vanilla, chocolate, maple, or none: ").lower() #Choosing flavor
        if flavoring == "vanilla" or flavoring == "v":
            costFlavoring = VANILLA_PRICE
            flavoring = "vanilla"
        elif flavoring == "chocolate" or flavoring == "c":
            costFlavoring = CHOCOLATE_PRICE
            flavoring = "chocolate"
        elif flavoring == "maple" or flavoring == "m":
            costFlavoring = MAPLE_PRICE
            flavoring = "maple"
        elif flavoring == "none" or flavoring == "n":
            costFlavoring = 0.00
            flavoring = "no"
        else:
            print("Sorry, we don't have that flavor.")
            quit()
    elif drink == "tea":
        flavoring = input("Please choose from one of the following flavor options: lemon, mint, or none: ").lower()
        if flavoring == "l" or flavoring == "lemon":
            costFlavoring = LEMON_PRICE
            flavoring = "lemon"
        if flavoring == "m" or flavoring == "mint":
            costFlavoring = MINT_PRICE
            flavoring = "mint"
        if flavoring == "n" or flavoring == "none":
            costFlavoring = 0.00
            flavoring = "no"
        else:
            print("Sorry, we don't have that flavour.")
            quit()
else:
    print("Sorry, we don't sell that drink.")
    quit()
tax = 1.11 #Defining tax to be multiplied.
totalCost = tax * (costSize + costFlavoring)  #Calculating total cost with tax
totalCost = round(totalCost, 2)  #Rounding total cost to 2 decimal points
print("For", name + ", a", size, drink + ",", flavoring, "flavoring, cost: $", str(totalCost)) #Final statement
