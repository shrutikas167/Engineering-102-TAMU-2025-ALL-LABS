# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SHRUTIKA SURESH
# Section: 503/504
# Assignment: Lab Topic 1
# Date: 29 08 2025
#
#
print ("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")

print ("My guess is 1.5")

import math
x = 1
print ((1-math.cos(x))/(x**2))
# Just using the same func; basically a loop * 0.1
x = 0.1
print ((1-math.cos(x))/(x**2))
#
x = 0.01
print ((1-math.cos(x))/(x**2))
#
x = 0.001
print ((1-math.cos(x))/(x**2))
#
x = 0.0001
print ((1-math.cos(x))/(x**2))
#
x = 0.00001
print ((1-math.cos(x))/(x**2))
#
x = 0.000001
print ((1-math.cos(x))/(x**2))
#
x = 0.0000001
print ((1-math.cos(x))/(x**2))

print ()

print ("My guess was about 1 off.")