import numpy
import math
import numpy as np
import random
from matplotlib import pyplot as plt

NUM_OF_POINTS = 100
W = 100
H = int(math.sqrt((W)**2-(W/2)**2))
slope = math.sqrt(3)

rotate_point_r = (W/4, H/2)
rotate_point_l = (-W/4, H/2)

def distance(point_1, point_2):
    base = (point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2
    return math.sqrt(base)

print(distance((5,5),(4,2)))

def dist_from_vertex(x_y_vertexs, point):
    min_dis = W #it cant be bigger than H/2
    for i, vertex in enumerate(x_y_vertexs):
       if distance(vertex, point) < min_dis: 
           min_dis = distance(vertex, point)
           index = i
        
    return index, min_dis

#vectext_list = [[-W/2,H/2],[W/2,H/2],[W/2,0]]
#a = dist_from_vertex(vectext_list, (W/2+10,H/2+20))

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

def project(point):
    line_l_rp = [(H/(W/2)), H/4]
    line_r_rp = [-(H/(W/2)), H/4]

    if point[0] < 0:
        point = [line_l_rp[0] - (point[0] - line_l_rp[0]), line_l_rp[1] - (point[1] - line_l_rp[1])]
    else:
        point = [line_r_rp[0] - (point[0] - line_r_rp[0]), line_r_rp[1] - (point[1] - line_r_rp[1])]
    
    xh = point[0] 
    return point

p2 = makePoint(H,W,rotate_point_l, rotate_point_r)
p2 = (-20,35)
p1 = project(p2)
# points = np.zeros((NUM_OF_POINTS,2), dtype='int64')
# print(points)

# for i in range(NUM_OF_POINTS):
#     points[i] = makePoint(H, W, rotate_point_l, rotate_point_r)

# print(points[0].var())
# plt.scatter(points[:, 0], points[:, 1])

plt.scatter([p1[0]], [p1[1]])
plt.axline((0,H),slope=(-H/(W/2)))
plt.axline((0,H),slope=(H/(W/2)))
plt.scatter([p2[0]], [p2[1]], color="red")
plt.axline(((W/2),0),slope=-(1/(H/(W/2))))
plt.axline(((-W/2),0),slope=(1/(H/(W/2))))

plt.grid(True)
plt.ylim(-50,H+30)
plt.xlim(-50,W+30)
plt.show()
