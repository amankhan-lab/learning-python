# arithematic math operator
import math

# Calcuulation of power differences

x = float(input("Enter the number: "))
y = float(input("Enter the number: "))

result = pow(x, y) - pow(y, x)

print(f"The difference between x and y is: {result}")
