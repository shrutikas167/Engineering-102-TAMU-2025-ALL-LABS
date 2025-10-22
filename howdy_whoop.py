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
def howdy_whoop(first_int, second_int):
    for i in range(1, 101):
        if i % first_int == 0 and i % second_int == 0:
            print("Howdy Whoop")
        elif i % first_int == 0:
            print("Howdy")
        elif i % second_int == 0:
            print("Whoop")
        else:
            print(i)

num1 = int(input('Enter an integer: '))
# done
num2 = int(input('Enter another integer: '))
howdy_whoop(num1, num2)