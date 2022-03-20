from os import rmdir
from pyexpat.model import XML_CQUANT_REP
import numpy as np
import matplotlib.pyplot as plt
import random
import math

"""One of the key assumtions to make this code simpler is that the middle points is at 0x"""
def lines_from_triange(points):
    """creates lines must be presented in order of right-middle-left"""
    right_line_fnc = lambda x: -x*(points[1][1]/points[0][0])+points[1][1]
    left_line_fnc = lambda x: -x*(points[1][1]/points[2][0])+points[1][1]
    return right_line_fnc, left_line_fnc

def flip_over_midpoint(midpoint, point):
    point = [midpoint[0] - (point[0] - midpoint[0]), midpoint[1] - (point[1] - midpoint[1])]
    return point

def calulate_midpoints(points):
    """creates midpoints must be presented in order of right-middle-left"""
    right_midpoint = [points[0][0]/2, points[1][1]/2]
    left_midpoint = [points[2][0]/2, points[1][1]/2]
    return right_midpoint, left_midpoint

def run_point(point, triangle_points, fncs, mids):
    """fncs and mids are diliverd (left, right)"""
    point[0] = (random.random()*(triangle_points[2][0]-triangle_points[0][0]))-triangle_points[0][0]
    point[1] = random.random() * triangle_points[1][1]

    if point[0] < 0:
        current_fnc = fncs[0]
        mid = mids[0] 
    else: 
        current_fnc = fncs[1] 
        mid = mids[1] 
        
    if point[1] > current_fnc(point[0]):
        point = flip_over_midpoint(mid, point)

    return point, current_fnc(point[0])

def run_points(x_tri_points, y_tri_points, num_of_points):
    points = np.zeros((num_of_points, 2))
    y_tri_points_tmp = y_tri_points.copy()

    x_point = np.zeros(2,)
    y_point = np.zeros(2,)

    eq_fncs = lines_from_triange(x_tri_points)
    eq_mids = calulate_midpoints(x_tri_points)
    
    y_tri_dist =  y_tri_points[0][0] - y_tri_points[2][0]
    # y_tri_dist = 1

    for i in range(num_of_points):
        x_point, scaler = run_point(x_point, x_tri_points, eq_fncs, eq_mids)
        y_tri_points_tmp[0][0] = (y_tri_dist * scaler) + y_tri_points[2][0]
        y_tri_points_tmp[1][1] = y_tri_points[1][1] - y_tri_points[2][0] * scaler
        y_fncs = lines_from_triange(y_tri_points_tmp)
        y_mids = calulate_midpoints(y_tri_points_tmp)
        y_point, scaler = run_point(y_point, y_tri_points_tmp, y_fncs, y_mids)

        points[i][0] = x_point[0]
        points[i][1] = y_point[0]
    
    return points

def run_tri_points(num_of_points, tri_points):
    out_points = np.zeros((num_of_points, 2))

    y_fncs = lines_from_triange(tri_points)
    y_mids = calulate_midpoints(tri_points)

    p = np.zeros(2,)
    for i in range(num_of_points):
        run_point(p, tri_points, y_fncs, y_mids)
        out_points[i][0] = p[0]
        out_points[i][1] = p[1]

    return out_points
        

q = math.sqrt(3)/2
points_x = np.array([[-0.5,0],[0,math.sqrt(3)/2],[0.5,0]])
points_y = np.array([[-q*(2/3),0],[0,q],[q*(1/3),0]])

num_of_points = 10000

points = run_points(points_x, points_y, num_of_points)
# points = run(1000, points_y)
fig = plt.figure()
plt.scatter([points[:, 0]], [points[:, 1]], color='red',s =2)

#Graphing
lfnc, rfnc = lines_from_triange(points_y)
lmid, rmid = calulate_midpoints(points_y)

plt.plot([-1,0],[lfnc(-1),lfnc(0)])
plt.plot([1,0],[rfnc(1),rfnc(0)])

plt.axis([points_x[0][0],points_x[2][0],0,1])

plt.scatter([lmid[0]], [lmid[1]], color='red')
plt.scatter([rmid[0]], [rmid[1]], color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
