from cmath import sqrt
from gettext import npgettext
from logging.handlers import RotatingFileHandler
from turtle import shape
import numpy
import math
import numpy as np
import random
from matplotlib import pyplot as plt

NUM_OF_POINTS = 100
W = 100
H = int(math.sqrt((W/2)**2-(W/4)**2))
slope = math.sqrt(3)

rotate_point_r = (W/4, H/2)
rotate_point_l = (-W/4, H/2)

def makePoint(H,W,rp_l, rp_r):
    p_1 = [random.randint(-W/2,W/2), random.random()*H]

    if p_1[0]>0:
        slope = -H/(W/2)
        rp = rp_r
    else:
        slope = H/(W/2)
        rp = rp_l

    if (p_1[1] > p_1[0]*slope+H):
        dist_x = p_1[0] - rp[0]
        dist_y = p_1[1] - rp[1]
        p_1 = (rp[0] - dist_x, rp[1] - dist_y)
        
    return p_1


points = np.zeros((NUM_OF_POINTS,2), dtype='int64')
print(points)

for i in range(NUM_OF_POINTS):
    points[i] = makePoint(H, W, rotate_point_l, rotate_point_r)

print(points[0].var())
plt.scatter(points[:, 0], points[:, 1])
# plt.axline((H,0),(0,W))
plt.axline((0,H),slope=(-H/(W/2)))
plt.axline((0,H),slope=(H/(W/2)))

plt.grid(True)
plt.ylim(-50,H+30)
plt.xlim(-50,W+30)
plt.show()
