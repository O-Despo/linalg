from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import numpy as np
import random
import math

"""One of the key assumtions to make this code simpler is that the middle points is at 0x"""
def calc_fncs(points, components=False):
    """creates lines must be presented in order of right-middle-left"""
    l_slope = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])
    l_intercept = points[1][1]
    r_slope = ((points[1][1]-points[2][1])/(points[1][0]-points[2][0]))
    r_intercept = points[1][1]
    if components:
        return (l_slope, l_intercept), (r_slope, r_intercept)
    else:
        return  lambda x: x*l_slope+l_intercept, lambda x: x*r_slope+r_intercept

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

def run_line_point():
    p = [random.random(),random.random()]

    if p[1] < p[0]:
        p = flip_over_midpoint((0.5, 0.5), p)

    return p

def run_point(triangle_points, fncs, mids):
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

    if point[1] > fnc(point[0]):
        point_out = flip_over_midpoint(mid, point)
    else:
        point_out = point

    return point_out, fnc(point_out[0])

def run_points(x_tri_points, y_tri_points, num_of_points):
    points = np.zeros((num_of_points, 2))
    y_tri_points_tmp = y_tri_points.copy()

    x_fncs = calc_fncs(x_tri_points)
    x_mids = calulate_midpoints(x_tri_points)
    
    for i in range(num_of_points):
        x_point, scaler = run_point(x_tri_points, x_fncs, x_mids)

        y_tri_points_tmp = y_tri_points * scaler
        
        y_fncs = calc_fncs(y_tri_points_tmp)
        y_mids = calulate_midpoints(y_tri_points_tmp)

        y_point, scalr = run_point(y_tri_points_tmp, y_fncs, y_mids)

        points[i][0] = x_point[0]
        points[i][1] = -(y_point[0] - y_tri_points_tmp[2][0])
        # points[i][1] = random.triangular(0,q,q*(1/3)) * scaler
    
    return points

def flip_over_line(slope, y_intercept, p1):
    d = (p1[0] + (p1[1] - y_intercept)*slope)/(1+slope**2)
    
    p1 = [round(2*d - p1[0], 8),round(2*d*slope - p1[1] + 2*y_intercept, 8)]
    return p1

def run_tri_points(num_of_points, tri_points):
    out_points = np.zeros((num_of_points, 3))
    l_line, r_line = calc_fncs(tri_points, components=True)
    fncs = (lambda x: x*l_line[0]+l_line[1], lambda x: x*r_line[0]+r_line[1])
    mids = calulate_midpoints(tri_points)

    z_fnc = lambda x: x*(tri_points[1][1]/((tri_points[2][0]-tri_points[0][0])/3)) 

    for i in range(num_of_points):
        p, q = run_point(tri_points, fncs, mids)
        a = run_line_point()
        p = [p[0], q*a[1]]

        dist_to_x = p[1]
        z = round(random.random()*z_fnc(dist_to_x), 8)

        choice = random.random()
        if choice < 1/3:
            p = flip_over_line(l_line[0], l_line[1], p)
        elif choice < 2/3:
            p = flip_over_line(r_line[0], r_line[1], p)

        out_points[i] = [round(p[0], 8), round(p[1], 8), z]

    return out_points
        
q = math.sqrt(3)/2
points_x = np.array([[-0.5,0],[0,q],[0.5,0]])
points_x_sub = np.array([[-0.5,0],[0,q*(1/3)],[0.5,0]])

points_y = np.array([[-q*(2/3),0],[0,q],[q*(1/3),0]])

num_of_points = 25000

#Test lines from triangle
line_fncs = calc_fncs(points_x)


#Graphing
fig = plt.figure()
ax = plt.axes(projection='3d')

points_in_use = points_x
lfnc, rfnc = calc_fncs(points_in_use)
lmid, rmid = calulate_midpoints(points_in_use)

# plt.plot([-1,0],[lfnc(-1),lfnc(0)], color="red")
# plt.plot([1,0],[rfnc(1),rfnc(0)], color="blue")

# lfnc, rfnc = lines_from_triange(points_x_sub)
# plt.plot([-1,0],[lfnc(-1),lfnc(0)], color="red")
# plt.plot([1,0],[rfnc(1),rfnc(0)], color="blue")


# Testing 0 1 distrobution
# plt.axline((0,0),(1,1))
# lmid = (0.5, 0.5)

# points = np.empty((num_of_points,2))
# for i in range(num_of_points):
#     points[i] = run_line_point()

# plt.scatter([lmid[0]], [lmid[1]], color='red')
# plt.scatter([points[:, 0]], [points[:, 1]], color='blue', alpha=0.2)

#Debug run point_
# p, z, q = run_point(points, (lfnc, rfnc), (lmid, rmid), True)
# plt.scatter([p[0]], [p[1]], color='red')
# plt.scatter([z[0]], [z[1]], color='blue')

#Debug flip over line
# p1 = (0.4, 4)
# p2 = flip_over_line(-2, 0.2, p1)
# print(p1, p2)
# plt.scatter([p1[0], p2[0]], [p1[1], p2[1]])
# plt.axline([0,0.5],[1,1], color="red")
# plt.axis([0,1,0,1])

#Debug run tri 3D
graph_points = run_tri_points(num_of_points, points_x_sub)
# plt.scatter([graph_points[:, 0]], [graph_points[:, 1]], color='blue', alpha=0.2)

v = np.array([(-0.5, 0, 0), (0.5, 0, 0), (0, points_in_use[2][0]-points_in_use[0][0], 0), (0, 1/3, math.sqrt(1/3**2))])
verts = [ [v[0],v[1],v[2]], [v[0],v[1],v[3]],
 [v[0],v[2],v[3]], [v[1],v[2],v[3]]]

ax.scatter(graph_points[:, 0], graph_points[:, 1], graph_points[:, 2], color="blue", alpha=0.2)
ax.add_collection3d(Poly3DCollection(verts, facecolors='r', linewidths=1, edgecolors='r', alpha=.0))


# #Debug run all
# points_graph = run_points(points_x, points_y, num_of_points)
# plt.scatter([points_graph[:, 0]], [points_graph[:, 1]], color='blue', alpha=0.05)

# plt.scatter([lmid[0]], [lmid[1]], color='red')
# plt.scatter([rmid[0]], [rmid[1]], color='blue')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
