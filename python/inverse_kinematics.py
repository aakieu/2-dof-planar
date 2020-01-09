from numpy import *

a1 = 6.2  # length of link a1 in cm
a2 = 5.2  # length of link a2 in cm
a3 = 0  # length of link a3 in cm
a4 = 7  # length of link a4 in cm

# Desired Position of End effector
x = -7
y = 9

# Equations for Inverse kinematics
r1 = sqrt(x**2+y**2)  # eqn 1
phi_1 = arccos((a4**2-a2**2-r1**2)/(-2*a2*r1))  # eqn 2
phi_2 = arctan2(y, x)  # eqn 3
theta_1 = rad2deg(phi_2-phi_1)  # eqn 4 converted to degrees

phi_3 = arccos((r1**2-a2**2-a4**2)/(-2*a2*a4))
theta_2 = 180-rad2deg(phi_3)

print('theta one: ', theta_1)
print('theta two: ', theta_2)

