# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: 
# Gianni Giacoman
# Johanna Serrano
# Pranav Shankar
# Shrutika Suresh
# Section: 406/407
# Assignment: Lab Topic 3 Team
# Date: 9 / 16 / 2025

time_1=float(input("Enter time 1: "))

x_pos=float(input("Enter the x position of the object at time 1: "))

y_pos=float(input("Enter the y position of the object at time 1: "))

z_pos=float(input("Enter the z position of the object at time 1: "))

time_2=float(input("Enter time 2: "))

x_pos2=float(input("Enter the x position of the object at time 2: "))

y_pos2=float(input("Enter the y position of the object at time 2: "))

z_pos2=float(input("Enter the z position of the object at time 2: "))


dt= (time_2-time_1)/4

# Interpolation - 1
t1=time_1


slope1=((x_pos2-x_pos)/(time_2-t1))

x1= slope1 * (t1 -time_1 ) + x_pos


slope2=((y_pos2-y_pos)/(time_2-t1))
y1= slope2 * (t1 -time_1 ) + y_pos


slope3=((z_pos2-z_pos)/(time_2-t1))
z1= slope3 * (t1 -time_1 ) + z_pos



print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

#Interpolation - 2 
t1=time_1+dt


x1= slope1 * (t1 -time_1 ) + x_pos


y1= slope2 * (t1 -time_1 ) + y_pos


z1= slope3 * (t1 -time_1 ) + z_pos


print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

# Interpolation - 3
t1=time_1+(2*dt)


x1= slope1 * (t1 -time_1 ) + x_pos


y1= slope2 * (t1 -time_1 ) + y_pos


z1= slope3 * (t1 -time_1 ) + z_pos


print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

# Interpolation - 4 
t1=time_1+(3*dt)


x1= slope1 * (t1 -time_1 ) + x_pos


y1= slope2 * (t1 -time_1 ) + y_pos


z1= slope3 * (t1 -time_1 ) + z_pos


print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")


# Interpolation - 5 
t1=time_2


x1= slope1 * (t1 -time_1 ) + x_pos


y1= slope2 * (t1 -time_1 ) + y_pos


z1= slope3 * (t1 -time_1 ) + z_pos


print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

# FIN - Shrutika Suresh
