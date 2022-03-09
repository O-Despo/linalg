import math
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

X = 1000
Y = 1000
Z = 1000

POINTS = 1000
output = np.zeros((POINTS, 2))

pos_x = random.random_integers(0, X)
pos_z = random.random_integers(0, X)

def pos_y_constraint(new_x):
    if new_x > X/2:
        return Y/(-X/2)*new_x+(2*X)
    else: 
        return Y/(X/2)*new_x+0

pos_y = random.random_integers(0, pos_y_constraint(pos_x))
pos = np.array((pos_x, pos_y, pos_z))
print(pos)

corners = np.array([(0,0,0),(X,0,0),(X,0,Z),(0,0,Z),(-X/2,-Y,-Z/2)])

for i in range(POINTS):
    corner = corners[random.random_integers(0,2,size=(1,))][0]
    pos = ((pos[0] - corner[0])/2, (pos[1] -corner[1])/2)
    output[i] = pos

plt.scatter(output[:, 0], output[:, 1])
plt.show()

    # distance = math.sqrt((pos[0]-corner[0])**2 + (pos[1]-corner[1])**2)
    # slope = (pos[1]-corner[1])/(pos[0]-corner[0])
    # y_intercept = pos[0]-(pos[1] * slope)
    # output[i] = (slope*distance/2+y_intercept, distance/2)
