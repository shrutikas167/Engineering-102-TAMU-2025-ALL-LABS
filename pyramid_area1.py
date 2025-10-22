# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shrutika Suresh
# Section: 406/407
# Assignment: Lab Topic 7 - Individual
# Date: 10 / 21 / 2025

fullName = input('What is your name? ').strip()

def firstSyllable(fullName):
    vowels = 'aeiou'
    strList = [i for i in fullName.lower()]
    for j in range(len(strList)):
        if strList[j] in vowels:
            return fullName[j:].lower()
    return fullName.lower()

print(f'{fullName}, {fullName}, Bo-B{firstSyllable(fullName)}\nBanana-Fana Fo-F{firstSyllable(fullName)}\nMe Mi Mo-M{firstSyllable(fullName)}\n{fullName}!')