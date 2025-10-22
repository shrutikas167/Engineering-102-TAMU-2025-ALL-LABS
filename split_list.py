# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shrutika Suresh
# Section: 406/407
# Assignment: Lab Topic 7 - Individual
# Date: 10 / 21 / 2025

#comment
try:
    myList = [int(i) for i in input('Enter numbers: ').split()]
except ValueError:
    quit('Hello professor\ni would have written this in a def and used return instead of quit() \nbut i realized this when i had already finished')
leftSum = 0
rightSum= 0
r = 0
while True:
    leftSum = 0
    rightSum= 0
    for i in myList[0:r]:
        leftSum+=int(i)
    for i in myList[r:]:
        rightSum+=int(i)
    if leftSum == rightSum:
        break
    if r>=len(myList):
        print('Cannot split evenly')
        quit()
    r+=1
print(f'Left: {myList[:r]}\nRight: {myList[r:]}\nBoth sum to {leftSum}')