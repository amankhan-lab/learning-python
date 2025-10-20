
Name = input("Please Enter your name:")
age = int(input(f"Please Enter your age:"))
print(f"Hello {Name}")
age = age + 1
print(f"Your age is {age}")

mass = float(input("Enter your mass: "))
g = 9.81
weight = mass * g
print(f"{Name}, Your Weight on Earth is {round (weight, 2)}")

#KINETIC ENERGY OF A MATERIAL

mass = float(input("please Enter your mass:"))
velocity = float(input("please enter your velocity:"))
kinetic_energy = 0.5 * mass / velocity ** 2
print(f"your kinetic energy is: {round (kinetic_energy, 2)}")

#POTENTIAL ENERGY OF AN OBJECT

mass = int(input("please enter the mass of the object:"))
g = 9.8
height = int(input("please enter the height of the object:"))

potential_energy = mass * g * height
print(f"Your Potential energy is: {round(potential_energy, 2)}")