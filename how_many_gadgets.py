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
inputDay = int(input('Please enter a positive value for day: '))

if inputDay < 0:
    print("You entered an invalid number!")
    quit()

gadget = 0

# Days 1–10
gadget += 10 * min(inputDay, 10)

# Days 11–50
if inputDay > 10:
    last = min(inputDay, 50)
    first = 11
    terms = last - 10
    gadget += (first + last) * terms // 2

# Days 51–100
if inputDay > 50:
    gadget += 50 * (min(inputDay, 100) - 50)

# Days >100 add nothing (net zero)

print(f'The sum total number of gadgets produced on day {inputDay} is {gadget}')