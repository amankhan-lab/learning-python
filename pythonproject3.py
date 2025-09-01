# Typecasting : THe process of converting a value of one data type to anotherr 
# (string, integerr, float, boolean)
#  Exiplicit VS Implicit

# EXPLICIT METHOD

name = "bro"
age = 0
gpa = 1.9
student = True


# classifying Data types

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))


# CONVERSION

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age)
print(type(age))

name = bool(name)
print(name)
print(type(name))

gpa = bool(gpa)
print(gpa)
print(type(gpa))

name = int(name)
print(name)
print(type(name))

age = str(age)
print(age)
print(type(age))

# NOTE: these are attach to each other meaning if you converts integeer to boolean and then to strings then your
# integer first works as aboolean before converting to string means only true or false

# IMPLICIT METGOD: this method is about converting variables data types automatically
#  it is when a value or variable converted into different data types automatically

x = 4
y = 2

print(x / y)
print(type(x))
print(type(y))
print(type(x / y))




