#SHOPPING CART PROGRAM

item = input("enter your order here: ")
price = float(input("Enter the price of an irtem you bought: "))
quantity = int(input("enter the quantity of an item: "))

total_cost = quantity * price

print(f"you bought {quantity}x {item}, your tootal cost is ${round(total_cost, 2)}")