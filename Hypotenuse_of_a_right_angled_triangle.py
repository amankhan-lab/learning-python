# arithematic math operator
import math

# Hypotenuse of a right angled triangle : c = sqrt of a square and b square

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of a right angled triangle is: {round(c, 2)}cm")