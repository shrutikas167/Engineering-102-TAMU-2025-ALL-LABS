# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SHRUTIKA SURESH
# Section: 406/506
# Assignment: Lab 6 - Idividual
# Date: 10/07/2025
#
#
import math
#start
n = int(input('Enter a positive integer: '))
nums = [n]
print(f'The Juggler sequence starting at {n} is: ')
while n!=1:
    if n%2==0:
        n = math.floor(math.sqrt(n))
    else:
        n=math.floor(n**1.5)
    nums.append(n)
print(', '.join(map(str, nums)))
print(f'It took {len(nums)-1} iterations to reach 1')