from os import rmdir
import numpy as np
import matplotlib.pyplot as plt
import random

"""One of the key assumtions to make this code simpler is that the middle points is at 0x"""
def lines_from_triange(points):
    """creates lines must be presented in order of right-middle-left"""
    right_line_fnc = lambda x: -x*(points[1][1]/points[0][0])+points[1][1]
    left_line_fnc = lambda x: -x*(points[1][1]/points[2][0])+points[1][1]
    return left_line_fnc, right_line_fnc

def flip_over_midpoint(midpoint, point):
    point = [midpoint[0] - (point[0] - midpoint[0]), midpoint[1] - (point[1] - midpoint[1])]
    return point

def calulate_midpoints(points):
    """creates midpoints must be presented in order of right-middle-left"""
    right_midpoint = [points[0][0]/2, points[1][1]/2]
    left_midpoint = [points[2][0]/2, points[1][1]/2]
    return right_midpoint, left_midpoint

def run_points(triangle_points, num_new_points):
    lfnc, rfnc = lines_from_triange(triangle_points)
    lmid, rmid = calulate_midpoints(triangle_points)

    new_points = np.zeros((num_new_points, 2))
    for i in range(num_new_points):
        x = (random.random()*(triangle_points[2][0]-triangle_points[0][0]))+triangle_points[0][0]
        y = random.random() * triangle_points[1][1]
        new_point = [x, y]

        if new_point[0] < 0:
            current_fnc = rfnc
            mid = lmid
        else: 
            current_fnc = lfnc
            mid = rmid
        
        if new_point[1] > current_fnc(new_point[0]):
            new_point = flip_over_midpoint(mid, new_point)

        new_points[i] = new_point

    return new_points

points_x = [[-0.5,0],[0,1],[0.5,0]]
points_y = [[-2/3,0],[0,1],[1/3,0]]

num_of_points = 1000
new_points_x = run_points(points_x, num_of_points)
new_points_y = run_points(points_y, num_of_points)

new_points = np.zeros((num_of_points, 2))
# new_points[:, 0] = new_points_y[:, 0]
# new_points[:, 1] = new_points_y[:, 0]
fig = plt.figure()
plt.scatter(new_points_x[:, 0], new_points_y[:, 0], color='blue')


#Graphing
lfnc, rfnc = lines_from_triange(points_x)
lmid, rmid = calulate_midpoints(points_x)


plt.plot([1,0],[lfnc(1),lfnc(0)])
plt.plot([-1,0],[rfnc(-1),rfnc(0)])

plt.axis([points_x[0][0],points_x[2][0],0,1])

plt.scatter([lmid[0]], [lmid[1]], color='red')
plt.scatter([rmid[0]], [rmid[1]], color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
