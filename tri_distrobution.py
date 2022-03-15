from cmath import sqrt
from gettext import npgettext
from logging.handlers import RotatingFileHandler
from turtle import shape
import numpy
import math
import numpy as np
import random
from matplotlib import pyplot as plt

NUM_OF_POINTS = 1000
W = 100
H = 100

rotate_point = (H/2, W/2)

def makePoint(H,W,rotate_point):
    p_1 = [random.random()*W, random.random()*W]

    if (p_1[1] > p_1[0]*(W/-H)+H):
        dist_x = p_1[0] - rotate_point[0]
        dist_y = p_1[1] - rotate_point[1]
        p_1 = (rotate_point[0] - dist_x, rotate_point[1] - dist_y)
        
    return p_1

def makePointbad(H,W):
    x = random.random()*W
    y = random.random()*(x*(H/-W)+H)
    return [x,y]

points_distro = np.zeros((NUM_OF_POINTS,2), dtype='int64')
points_no_distro = np.zeros((NUM_OF_POINTS,2), dtype='int64')

for i in range(NUM_OF_POINTS):
    points_no_distro[i] = makePointbad(H, W)
    points_distro[i] = makePoint(H, W, rotate_point)

plt.scatter(points_no_distro[:, 0], points_no_distro[:, 1], color="blue")
plt.scatter(points_distro[:, 0], points_distro[:, 1], color="green")
# plt.axline((H,0),(0,W))
plt.axline((0,H),slope=(-H/W))
plt.grid(True)
plt.ylim(0,H)
plt.xlim(0,H)
plt.show()
