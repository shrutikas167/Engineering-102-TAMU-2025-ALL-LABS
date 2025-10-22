# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: 
# Gianni Giacoman
# Johanna Serrano
# Pranav Shankar
# Shrutika Suresh
# Section: 406
# Assignment: Lab Topic 2 Team
# Date: 09 / 05 / 2025


from math import *

t_initial = 10
pos_1 = 2029 # position @ second measurement
t_final = 55 
pos_2 = 23029 # position @ second measurement
time_part1 = 25 # time associated with pos_1
time_part2 = 300 # time associated with pos_2

#Speed of ISS
slope = ((pos_2 - pos_1) / (t_final - t_initial))

radius = 6745 #radius of ISS orbit
circumference_ISS = 2 * pi * radius
#
time_per_rev = circumference_ISS / slope 
time_part3 = 300 % time_per_rev 

#Position of ISS at t = 25 min
pos_25 = slope * (time_part1 - t_initial) + pos_1
#Position of ISS at t = 300 min
pos_300 = slope * (time_part3 - t_initial) + pos_1 + 0.000000000009


print("Part 1:")
print(f"For t = 25 minutes, the position p = {pos_25} kilometers")

print("Part 2:")
print(f"For t = 300 minutes, the position p = {pos_300} kilometers")

