from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

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
verts = np.array([
    [tetra_vertex[0],tetra_vertex[1],tetra_vertex[2]],
    [tetra_vertex[0],tetra_vertex[1],tetra_vertex[3]],
    [tetra_vertex[0],tetra_vertex[2],tetra_vertex[3]],
    [tetra_vertex[1],tetra_vertex[2],tetra_vertex[3]]
])


# Graphing
fig = plt.figure()
ax = plt.axes(projection='3d')

# ax.set_box_aspect([
#     tetra_vertex[0][0],
#     tetra_vertex[2][0],
#     tetra_vertex[0][0],
#     tetra_vertex[1][1],
#     tetra_vertex[0][0],
#     tetra_vertex[3, 2]
#     ])

ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0,1)
ax.set_zlim3d(0,1)
# ax.set_box_aspect([1, 1, 5])

ax.add_collection3d(Poly3DCollection(verts, facecolors='r', linewidths=1, edgecolors='r', alpha=.0))

ax.scatter(tetra_vertex[:, 0], tetra_vertex[:, 1], tetra_vertex[:, 2])
plt.show()