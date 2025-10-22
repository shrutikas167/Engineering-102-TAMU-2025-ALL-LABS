# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: SHRUTIKA SURESH
# Section: 406/506
# Assignment: Lab 3 - Idividual
# Date: 19/09/2025
#
import math
def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')
side_length = float(input('Please enter the side length: '))
printresult('triangle', side_length, math.sqrt(3)/4*side_length**2)
printresult('square', side_length, side_length**2)
printresult('pentagon', side_length, 1/4*math.sqrt(5*(5+2*math.sqrt(5)))*side_length**2)
printresult('hexagon', side_length, (3*math.sqrt(3))/2*side_length**2)
printresult('dodecagon', side_length, 3*side_length**2*(2+math.sqrt(3)))
# comment