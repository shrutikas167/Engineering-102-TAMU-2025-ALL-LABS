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

import math

def approximating_ln():
    print("Enter a value for x:")
    while True:
        x = float(input())
        if 0 < x <= 2:
            break
        else:
            print("Out of range! Try again:")

    print("Enter the tolerance:")
    tol = float(input())

    n = 1
    term = (x - 1)
    approx = 0
    while abs(term) >= tol:
        approx += term
        n += 1
        term = ((-1) ** (n + 1)) * ((x - 1) ** n) / n

    exact = math.log(x)

    # FINALLY i got the 0.0 to show up
    print(f"ln({x}) is approximately {approx if approx != 0 else 0.0}")
    print(f"ln({x}) is exactly {exact}")
    print(f"The difference is {abs(approx - exact)}")

if __name__ == "__main__":
    approximating_ln()