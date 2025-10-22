# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shrutika Suresh
# Section: 406/407
# Assignment: Lab Topic 7 - Individual
# Date: 10 / 21 / 2025

fullName = input('What is your name? ').strip()

def firstSyllable(name):
    vowels = 'aeiouyAEIOUY'  # include 'y' as vowel for tricky cases like Bryan, Cynthia, Yvonne
    if name[0] in vowels:
        return name.lower()
    for i in range(1, len(name)):  # start from 1 so we don’t drop the first letter if it’s vowel
        if name[i] in vowels:
            return name[i:].lower()
    return name.lower()

y = firstSyllable(fullName)

print(f'{fullName}, {fullName}, Bo-B{y}')
print(f'Banana-Fana Fo-F{y}')
print(f'Me Mi Mo-M{y}')
print(f'{fullName}!')