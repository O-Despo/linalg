from cmath import sqrt
import matplotlib.pyplot as plt
import numpy as np
import random
import math

# make a triangle that is 1/3 the sixe of last choose x bassed on distrobution
# chosed y with distobution contatinat 
# 1/3 flip it

h = sqrt(3)/2
tri_points = np.array([
    [-0.5, 0.0],
    [0.0, h],
    [0.5, 0.0]
])

def get_funcs(points):
    # Input left-middle-right
    lfnc = lambda x : x*((points[1][1]-points[0][1])/(points[1][0]-points[0][0]))
    rfnc = lambda x : x*((points[1][1]-points[2][1])/(points[1][0]-points[2][0]))
    return lfnc, rfnc

def get_midpoint(points):
    # Input two points
    return [points[0][0]+points[1][0])/2, points[0][1]/points[1][1]]

#Graphing
lfnc, rfnc = get_funcs(tri_points)
plt.plot((tri_points[0][0], tri_points[1][0]),(lfnc(tri_points[0][0]), lfnc(tri_points[1][0])))
plt.plot((tri_points[2][0], tri_points[1][0]),(rfnc(tri_points[2][0]), rfnc(tri_points[1][0])))

lmid = get_midpoint((tri_points[0],tri_points[1]))
rmid = get_midpoint((tri_points[2],tri_points[1]))
plt.scatter([lmid[0],rmid[0]], [lmid[1],rmid[1]])
plt.show()