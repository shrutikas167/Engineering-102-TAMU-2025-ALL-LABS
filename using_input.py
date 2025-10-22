# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SHRUTIKA SURESH
# Section: 406/506
# Assignment: Lab 3 - Idividual
# Date: 11/09/2025
#
import math
print('This program calculates the Reynolds number given velocity, length, and viscosity\n')
vel = float(input('Please enter the velocity (m/s): \n'))
l  = float(input('Please enter the length (m): \n'))
visc = float(input('Please enter the viscosity (m^2/s): \n'))
print(f'Reynolds number is {round(vel*l/visc)}\n')
#SHortened all of the names of variables to make it easy for me 

print('This program calculates the wavelength given distance and angle\n')
dist = float(input('Please enter the distance (nm): \n'))
angle = math.radians(float(input('Please enter the angle (degrees): \n')))
print(f'Wavelength is {2*dist*math.sin(angle):.4f} nm\n')

print('\nThis program calculates the production rate given time, initial rate, and decline rate\n')
time = float(input('Please enter the time (days): \n'))
initial_rate = float(input('Please enter the initial rate (barrels/day): \n'))
decline_rate = float(input('Please enter the decline rate (1/day): \n'))
b = 0.8
print(f'Production rate is {initial_rate/pow(1+b*decline_rate*time, 1/b):.2f} barrels/day\n')

print('This program calculates the change of velocity given initial mass, final mass, and exhaust velocity\n')
initial_mass = float(input('Please enter the initial mass (kg): \n'))
final_mass = float(input('Please enter the final mass (kg): \n'))
exhaust_vel = float(input('Please enter the exhaust velocity (m/s): \n'))
print(f'Change of velocity is {exhaust_vel*math.log(initial_mass/final_mass):.1f} m/s')