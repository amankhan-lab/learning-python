# arithematic math operator
import math

# SIMPLE INTEREST 

principal = int(input("Enter you principal: "))
Rate_of_interest = float(input("Enter your rate of interest: "))
Time_period = int(input("Enter Time period: "))

Simple_interest = (principal * Rate_of_interest * Time_period) / 100

print(f"Your simple interest is {Simple_interest}")