# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SHRUTIKA SURESH
# Section: 407/507
# Assignment: Lab 2 - Idividual
# Date: 11/09/2025
#
#
import math
u = 9
L = 0.875
v = 0.0015
uL = u*L
Re = uL/v # Split into two parts because I was lazy
print ("Reynolds number is", Re)
#
deg = 35
rad = math.radians(deg)
result = math.sin(rad)
wavelength = 2*0.029*result # Using result was kind of tedious; Might do res next time
print ("Wavelength is", wavelength, "nm")
#
t = 10
q = 100
d = 2
b = 0.8
arps_prod = q/((1+b*d*t)**(1/b)) # this actually worked??
print ("Production rate is", arps_prod, "barrels/day")
#
m_0 = 11000
m_final = 8300
vel = 2029
vel_change = vel * (math.log(m_0/m_final)) # Okay we got that on LOCK SLAYYYYYY
print ("Change of velocity is", vel_change, "m/s")