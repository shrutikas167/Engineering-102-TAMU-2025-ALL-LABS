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
# Assignment: Lab Topic 6 Team
# Date: 10 / 3 / 2025

cubeLength = float(input('Enter the side length in meters: '))
pyramidHeight = int(input('Enter the number of layers: '))

# Sum of areas for all visible side layers
# Each layer contributes i * cubeLength^2 per side → total = 4 * cubeLength^2 * (1+2+...+n)
sideArea = 4 * (cubeLength**2) * (pyramidHeight * (pyramidHeight + 1) / 2)

# Top area = cubeLength^2 (for the base layer’s top) + (n-1)*((cubeLength^2)*(pyramidHeight+1))
# Simplify directly:
topArea = (cubeLength**2) * (1 + (pyramidHeight - 1) * (pyramidHeight + 1))

# Total area
totalArea = sideArea + topArea

print(f'You need {totalArea:.2f} m^2 of gold foil to cover the pyramid')