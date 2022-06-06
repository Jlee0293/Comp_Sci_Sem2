x = int(input("How many items are you purchasing?")
total = 0
for i in range (0, x ):
    item = input("whats the item? ")
    price = float(input("What is the price of te item?"))
    print("Thanks for buying"+ item)
    total = total + price
print( " Your total is : " + str(total))
