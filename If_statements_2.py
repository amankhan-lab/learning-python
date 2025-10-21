# IF statement: Do some code IF condition is true else do something

decision = input("would you like to have a cup of coffee (Y/N): ")

if decision == "Y":            # == it means we compare the value equallly means decision is now Y means true
    print("Here is your coffee then")
elif decision == "N":
    print("No coffee for you!")
else: 
    print("sorry, the stock is over!")