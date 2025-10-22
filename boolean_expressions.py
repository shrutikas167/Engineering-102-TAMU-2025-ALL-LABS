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
# Assignment: Lab Topic 4 Team - boolean
# Date: 9 / 19 / 2025

############ Part A ############
a = input('Enter True or False for a: ')
b = input('Enter True or False for b: ')
c = input('Enter True or False for c: ')
a_True = a=="True" or a=='T' or a=='t'
b_True = b=="True" or b=='T' or b=='t'
c_True = c=="True" or c=='T' or c=='t'

# okay so I HAVE to do this the long way dang it

a_False = a=="False" or a=='F' or a=='f'
b_False = b=="False" or b=='F' or b=='f'
c_False = c=="False" or c=='F' or c=='f'

# this is so annoying

############ Part B ############
print('a and b and c: True'*(a_True and b_True and c_True)+
      'a and b and c: False' * (a_False or b_False or c_False))

print('a or b or c: True'*(a_True or b_True or  c_True)+
      'a or b or c: False'*(a_False and b_False and c_False))

############ Part C ############
print('XOR: True'*(a_True and b_False)+
      'XOR: True'*(a_False and b_True)+
      'XOR: False'*(a_True and b_True)+
      'XOR: False'*(a_False and b_False))

print('Odd number: True'*(a_True+b_True+c_True == 1 or a_True+b_True+c_True==3)+
      'Odd number: False'*(a_True+b_True+c_True == 2 or a_True+b_True+c_True==0))

# are you happy now???