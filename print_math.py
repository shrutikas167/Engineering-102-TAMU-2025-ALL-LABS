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
u = 9
v = 0.0015
L = 0.875
Re = (u*L)/v
print("Reynolds number is", Re)
#
#
d = 0.029
a = 35
import math # here I imported math pretty late remember to do that going forward
a_radians = math.radians (a)
sin_func = math.sin (a_radians)
print ("Wavelength is",(2*d*sin_func), "nm")
#
#
import math
q = 100
d = 2
b = 0.8
t = 10
print ("Production rate is",(q/((1+b*d*t)**(1/b))), "barrels/day")
#
# 
import math
v = 2029
m0 = 11000
mf = 8300
print ("Change of velocity is",(v*(math.log(m0/mf))), "m/s")
# HUZZAH last one done...tho this is already late lol