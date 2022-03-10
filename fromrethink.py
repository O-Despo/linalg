import matplotlib
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
import random
import math
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

xy_W = 1
xy_H = math.sqrt(xy_W**2 - (xy_W/2)**2)
yz_Q = math.sqrt(xy_H**2 - (xy_H/3)**2)

def make_point():
    xy_slope = -xy_H/(xy_W/2)
    yz_slope = yz_Q/(xy_H*(1/3))
    yz_inter = 0

    p = [random.random()- xy_W/2, random.random() * xy_H, random.random() * yz_Q]
    
    xyr = [xy_slope, xy_H/4]
    yx_rotate = [xy_H*(2/3), yz_Q/2]

    if p[0] < 0: 
        xyr[0] = -xyr[0]
        xy_slope = -xy_slope

    if p[1] > p[0]*xy_slope+xy_H:
        p = [xyr[0] - (p[0] - xyr[0]), xyr[1] - (p[1] - xyr[1]), p[2]]

    if p[1] < xy_H*(1/3)+yz_inter:
        yx_rotate[0] = [xy_H*(1/6)]
        yz_slope = yz_Q/(xy_H*(2/3))
        yz_inter = 2*yz_Q

    if p[2] > p[1]*yz_slope+yz_inter:
        p = [p[0], xyr[1] - (p[1] - xyr[1]), p[2]]

    return p

NUMBER_OF_POINTS = 100
p = np.zeros((NUMBER_OF_POINTS,3))

for i in range(NUMBER_OF_POINTS):
    p[i] = make_point()

ax.scatter([p[:, 0]], p[: ,1], p[:, 2])

v = np.array([(-xy_W/2, 0, 0), (xy_W/2, 0, 0), (0, xy_H, 0), (0, xy_H*(1/3), yz_Q)])
verts = [ [v[0],v[1],v[2]], [v[0],v[1],v[3]],
 [v[0],v[2],v[3]], [v[1],v[2],v[3]]]

for i in v:
    ax.scatter(i[0], i[1], i[2])
ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
plt.show()