print("Welcome customer")
size = input("What size of pizza would you like to buy small medium or large\n")
peperoni = input("would you like peperoni with it yes or no?\n")
cheese = input("Would you like cheese with it yess or no\n")
bill = 0
if size == "small":
    bill += 15
elif size == "medium":
    bill += 20
else:
    bill += 25
if peperoni == "yes" and size == "small":
    bill += 2
if peperoni == "yes" and size == "medium" or "large":
    bill += 3
if cheese == "yes":
    bill += 1
print(f"your final bill is ${bill}")
    
