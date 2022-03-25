from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import numpy as np
import random
import math

def mid_of(point, vertex):
    assert point.shape == vertex.shape

    for i in range(point.shape[0]):
        point[i] = (vertex[i] - point[i])/2 + point[i]
    
    return point

TRI = 1
tri_height = math.sqrt(TRI**2-(TRI/2)**2)
tetrahedron_height = math.sqrt(TRI**2-(tri_height/3)**2)

tri_base_vertex = [[-TRI/2, 0], [0, tri_height], [TRI/2, 0]]
tetra_vertex = [[vertex[0], vertex[1], 0] for vertex in tri_base_vertex]
tetra_vertex = np.array([
    [tri_base_vertex[0][0], tri_base_vertex[0][1], 0], 
    [tri_base_vertex[1][0], tri_base_vertex[1][1], 0], 
    [tri_base_vertex[2][0], tri_base_vertex[2][1], 0], 
    [0, TRI/3, tetrahedron_height]
])

num_of_points = 10000
out_points = np.zeros((num_of_points, 3))

current_point = np.array([0, .4, .5], dtype='float')
print(current_point, mid_of(current_point, tetra_vertex[0]))

for i in range(num_of_points):
    rand_ver = random.choice(tetra_vertex)
    current_point = mid_of(current_point, rand_ver)
    assert(current_point[1] < 0.9)
    out_points[i] = current_point

verts = np.array([
    [tetra_vertex[0],tetra_vertex[1],tetra_vertex[2]],
    [tetra_vertex[0],tetra_vertex[1],tetra_vertex[3]],
    [tetra_vertex[0],tetra_vertex[2],tetra_vertex[3]],
    [tetra_vertex[1],tetra_vertex[2],tetra_vertex[3]]
])

# Graphing
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0,1)
ax.set_zlim3d(0,1)
# ax.set_box_aspect([1, 1, 5])

ax.add_collection3d(Poly3DCollection(verts, facecolors='r', linewidths=1, edgecolors='r', alpha=.1))

ax.scatter(tetra_vertex[:, 0], tetra_vertex[:, 1], tetra_vertex[:, 2])
ax.scatter(out_points[:, 0], out_points[:, 1], out_points[:, 2])
plt.show()