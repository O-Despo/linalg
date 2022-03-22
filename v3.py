from os import rmdir
from pyexpat.model import XML_CQUANT_REP
from turtle import color
from xml.sax.handler import property_interning_dict
import numpy as np
import matplotlib.pyplot as plt
import random
import math

"""One of the key assumtions to make this code simpler is that the middle points is at 0x"""
def lines_from_triange(points):
    """creates lines must be presented in order of right-middle-left"""
    left_line_fnc = lambda x: x*(points[1][1]/-points[0][0])+points[1][1]
    right_line_fnc = lambda x: x*(points[1][1]/-points[2][0])+points[1][1]
    return  left_line_fnc, right_line_fnc

def flip_over_midpoint(midpoint, point):
    point = [midpoint[0] - (point[0] - midpoint[0]), midpoint[1] - (point[1] - midpoint[1])]
    return point

def calulate_midpoints(points):
    """creates midpoints must be presented in order of right-middle-left"""
    left_midpoint = [points[0][0]/2, points[1][1]/2]
    right_midpoint = [points[2][0]/2, points[1][1]/2]
    return left_midpoint, right_midpoint

def caclulate_midpoint_of_2p(points):
    midpoint = [points[0]/2, points[1]/2]
    return midpoint

def run_point(triangle_points, fncs, mids, debug=False):
    """fncs and mids are diliverd (left, right)"""
    point = np.zeros((2,))
    point[0] = (random.random()*(triangle_points[2][0]-triangle_points[0][0]))+triangle_points[0][0]
    point[1] = random.random() * triangle_points[1][1]

    if point[0] < triangle_points[1][0]:
        fnc = fncs[0]
        mid = mids[0] 
    else: 
        fnc = fncs[1]
        mid = mids[1] 

    # Clean for DEBUG 
    if point[1] > fnc(point[0]):
        point_out = flip_over_midpoint(mid, point)
    else:
        point_out = point

    if debug:
        return point_out, point, fnc(point_out[0])
    else:
        return point_out, fnc(point_out[0])

def run_points(x_tri_points, y_tri_points, num_of_points):
    points = np.zeros((num_of_points, 2))
    y_tri_points_tmp = y_tri_points.copy()

    x_fncs = lines_from_triange(x_tri_points)
    x_mids = calulate_midpoints(x_tri_points)
    
    for i in range(num_of_points):
        x_point, scaler = run_point(x_tri_points, x_fncs, x_mids)

        y_tri_points_tmp = y_tri_points * scaler
        
        y_fncs = lines_from_triange(y_tri_points_tmp)
        y_mids = calulate_midpoints(y_tri_points_tmp)

        y_point, scalr = run_point(y_tri_points_tmp, y_fncs, y_mids)

        points[i][0] = x_point[0]
        points[i][1] = -(y_point[0] - y_tri_points_tmp[2][0])
        # points[i][1] = random.triangular(0,q,q*(1/3)) * scaler
    
    return points

def run_tri_points(num_of_points, tri_points):
    out_points = np.zeros((num_of_points, 2))

    fncs = lines_from_triange(tri_points)
    mids = calulate_midpoints(tri_points)

    for i in range(num_of_points):
        p, q = run_point(tri_points, fncs, mids)
        out_points[i] = p

    return out_points
        
q = math.sqrt(3)/2
points_x = np.array([[-0.5,0],[0,q],[0.5,0]])
points_y = np.array([[-q*(2/3),0],[0,q],[q*(1/3),0]])

num_of_points = 60000

#Test lines from triangle
line_fncs = lines_from_triange(points_x)
fig = plt.figure()

#Graphing
points_in_use = points_x
lfnc, rfnc = lines_from_triange(points_in_use)
lmid, rmid = calulate_midpoints(points_in_use)

plt.plot([-1,0],[lfnc(-1),lfnc(0)], color="red")
plt.plot([1,0],[rfnc(1),rfnc(0)], color="blue")

plt.axis([points_in_use[0][0],points_in_use[2][0],0,1])

#Debug run point
# p, z, q = run_point(points_y, (lfnc, rfnc), (lmid, rmid), True)
# plt.scatter([p[0]], [p[1]], color='red')
# plt.scatter([z[0]], [z[1]], color='blue')

#Debug run tri
# pointss = run_tri_points(num_of_points, points_in_use)
# plt.scatter([pointss[:, 0]], [pointss[:, 1]], color='blue', alpha=0.2)

#Debug run all
points_graph = run_points(points_x, points_y, num_of_points)
plt.scatter([points_graph[:, 0]], [points_graph[:, 1]], color='blue', alpha=0.05)

plt.scatter([lmid[0]], [lmid[1]], color='red')
plt.scatter([rmid[0]], [rmid[1]], color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
