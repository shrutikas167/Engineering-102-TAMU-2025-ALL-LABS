# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SHRUTIKA SURESH
# Section: 406/506
# Assignment: Lab 4 - Idividual
# Date:23/09/2025
#
#
import math
# user input (done)
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

# set 0 as invalid input for a + b
if a == 0 and b == 0:
    print("You entered an invalid combination of coefficients!")
    quit()

# a = 0 is simple
if a == 0:
    p1 = -c / b
    print(f"The root is x = {p1}")
    quit()

#ugh hard part
p2 = b**2 - 4*a*c
if p2 > 0:
    x1 = (-b + math.sqrt(p2)) / (2*a)
    x2 = (-b - math.sqrt(p2)) / (2*a)
    print(f"The roots are x = {x1} and x = {x2}")
elif p2 == 0:
    p1 = -b / (2*a)
    print(f"The root is x = {p1}")
else:
    real = -b / (2*a)
    imaginary = math.sqrt(-p2) / (2*a)
    print(f"The roots are x = {real} + {imaginary}i and x = {real} - {imaginary}i")