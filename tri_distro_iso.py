from ctypes.wintypes import PPOINT
import numpy
import math
import numpy as np
import random
from matplotlib import pyplot as plt

NUM_OF_POINTS = 10
W = 100
# H = int(math.sqrt((W)**2-(W/2)**2))
slope = math.sqrt(3)

H = math.sqrt(W**2 - (W/2)**2)
Q = math.sqrt(H**2 - (H/3)**2)

rotate_point_r = (W/4, H/2)
rotate_point_l = (-W/4, H/2)

def distance(point_1, point_2):
    base = (point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2
    return math.sqrt(base)

def dist_from_vertex(x_y_vertexs, point):
    min_dis = W #it cant be bigger than H/2
    for i, vertex in enumerate(x_y_vertexs):
       if distance(vertex, point) < min_dis: 
           min_dis = distance(vertex, point)
           index = i
        
    return index, min_dis

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

#Iso lines 
plt.axline(([H*(2/3),Q/2]),slope= Q/-(H*(2/3)), color="orange")
plt.axline(([H*(1/6),Q/2]),slope= Q/(H*(1/3)), color="orange")

def makePoint_iso(H,W,rp_l, rp_r):
    p_1 = [random.random() * H, random.random()*Q]
    rp_l = [H*(2/3),Q/2]
    rp_r = [H*(1/6),Q/2]
    D = math.sqrt(Q**2 - (H*(1/3)**2))

    if p_1[0]>H*(1/3):
        slope = -Q/(H*(2/3))
        rp = rp_l

    else:
        slope = Q/(H*(1/3))
        rp = rp_r

    inter = (rp[1]/(slope*rp[0]))*10

    if (p_1[1] > p_1[0]*slope+inter):
        dist_x = p_1[0] - rp[0]
        dist_y = p_1[1] - rp[1]
        p_1 = (rp[0] - dist_x, rp[1] - dist_y)
        
    plt.axline((0,inter), slope=slope, color="red")
    return p_1
def project_equa(point):
    line_l_rp = [(H/(W/2)), H/4]
    line_r_rp = [-(H/(W/2)), H/4]

    if point[0] < 0:
        point = [line_l_rp[0] - (point[0] - line_l_rp[0]), line_l_rp[1] - (point[1] - line_l_rp[1])]
    else:
        point = [line_r_rp[0] - (point[0] - line_r_rp[0]), line_r_rp[1] - (point[1] - line_r_rp[1])]
    
    xh = point[0] 
    return point

def project_iso(point):
    line_l_rp = [(Q/(H*(2/3))), Q*2]
    line_r_rp = [-(Q/(H*(1/3))), 0]

    if point[0] < 0:
        point = [line_l_rp[0] - (point[0] - line_l_rp[0]), line_l_rp[1] - (point[1] - line_l_rp[1])]
    else:
        point = [line_r_rp[0] - (point[0] - line_r_rp[0]), line_r_rp[1] - (point[1] - line_r_rp[1])]
    
    return point

#p2 = makePoint(H,W,rotate_point_l, rotate_point_r)
#p2 = (-20,35)
#p1 = project(p2)
points = np.zeros((NUM_OF_POINTS,2), dtype='int64')
print(points)

for i in range(NUM_OF_POINTS):
    points[i] = makePoint_iso(H, W, rotate_point_l, rotate_point_r)

print(points[0].var())
plt.scatter(points[:, 0], points[:, 1])

plt.scatter([points[:, 0]], [points[:, 1]])

plt.axline((0,H),slope=(-H/(W/2)))
plt.axline((0,H),slope=(H/(W/2)))

plt.axline(((W/2),0),slope=-(1/(H/(W/2))))
plt.axline(((-W/2),0),slope=(1/(H/(W/2))))
plt.scatter(H*(1/3),Q)
plt.grid(True)
plt.ylim(-50,H+30)
plt.xlim(-50,W+30)
plt.show()
