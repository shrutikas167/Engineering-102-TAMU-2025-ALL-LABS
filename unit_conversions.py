# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Gianni Giacoman
# Johanna Serrano
# Pranav Shankar
# Shrutika Suresh
# Section: 406/407
# Assignment: Lab Topic 3 Team - Rounding
# Date: 9 / 18 / 2025

x = float(input("Please enter the quantity to be converted: "))

newtons = x*4.4482216153
print(f'{x:.2f} pounds force is equivalent to {newtons:.2f} newtons')

ft = x*3.28084
print(f'{x:.2f} meters is equivalent to {ft:.2f} feet')

kpa = x*101.325
print(f'{x:.2f} atmospheres is equivalent to {kpa:.2f} kilopascals')

BTU = x*3.412141623
print(f'{x:.2f} watts is equivalent to {BTU:.2f} BTU per hour')

gal = (x*60)/3.78541
print(f'{x:.2f} liters per second is equivalent to {gal:.2f} US gallons per minute')

fahrenheit = (x*9/5)+32
print(f'{x:.2f} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit')
# All names shortened except farenheit due to it not being a universal SI unit