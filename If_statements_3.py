# IF statement: Do some code IF condition is true else do something

name = input("Enter your name: ")
roll_no = input("Enter your roll no. : ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

if roll_no == "":
    print("you forgot to type your roll no.")
else:
    print(f"Your roll number is {roll_no}")