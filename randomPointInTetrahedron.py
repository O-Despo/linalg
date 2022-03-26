from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import numpy as np
import random
import math

"""One of the key assumtions to make this code simpler is that the middle points is at 0x"""

class randomPointInTetrahedron():
    """Produces random points in a tetrahedron without throwing our points
    Only uses equilateral base
    All triangle must be entered in left-middle-right format"""

    def __init__(self, tri_base_size):
        self.tri_base_size = tri_base_size 
        self.tri_h = math.sqrt(self.tri_base_size**2-(self.tri_base_size/2)**2)

        self.tri_base_points = np.array([
            [-self.tri_base_size/2, 0],
            [0, self.tri_h/3],
            [self.tri_base_size/2, 0]
            ])

        #Midpoints and functions
        self.mids = self.calulate_midpoints(self.tri_base_points)
        self.lcomps, self.rcomps, self.lfnc, self.rfnc = self.calc_fncs(self.tri_base_points)
        self.working_point = np.zeros((2,))
        self.ypoint = np.zeros((2,))

    def flip_over_midpoint(self, midpoint, point):
        point = [midpoint[0] - (point[0] - midpoint[0]), midpoint[1] - (point[1] - midpoint[1])]
        return point

    def calc_fncs(self, points):
        """creates lines must be presented in order of right-middle-left"""
        l_slope = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])
        l_intercept = points[1][1]
        r_slope = ((points[1][1]-points[2][1])/(points[1][0]-points[2][0]))
        r_intercept = points[1][1]
        
        return (l_slope, l_intercept), (r_slope, r_intercept), lambda x: x*l_slope+l_intercept, lambda x: x*r_slope+r_intercept

    def calulate_midpoints(self, points):
        """Creates midpoints must be presented in order of right-middle-left"""
        left_midpoint = [points[0][0]/2, points[1][1]/2]
        right_midpoint = [points[2][0]/2, points[1][1]/2]
        return left_midpoint, right_midpoint

    def run_line_point(self):
        self.ypoint[:] = random.random(), random.random()

        if self.ypoint[1] < self.ypoint[0]:
            self.ypoint = self.flip_over_midpoint((0.5, 0.5), self.ypoint)

        return self.ypoint

    def run_point(self):
        """fncs and mids are diliverd (left, right)"""
        self.working_point[0] = (random.random()*(self.tri_base_points[2][0]-self.tri_base_points[0][0]))+self.tri_base_points[0][0]
        self.working_point[1] = random.random() * self.tri_base_points[1][1]

        if self.working_point[0] < self.tri_base_points[1][0]:
            fnc = self.lfnc
            mid = self.mids[0]
        else: 
            fnc = self.rfnc
            mid = self.mids[1]

        if self.working_point[1] > fnc(self.working_point[0]):
            self.working_point = self.flip_over_midpoint(mid, self.working_point)
        else:
            self.working_point = self.working_point

        return self.working_point, fnc(self.working_point[0])

    def flip_over_line(self, slope, y_intercept, p1):
        d = (p1[0] + (p1[1] - y_intercept)*slope)/(1+slope**2)
        p1 = [round(2*d - p1[0], 8),round(2*d*slope - p1[1] + 2*y_intercept, 8)]
        return p1

    def run_points(self, num_of_points):
        out_points = np.zeros((num_of_points, 3))

        z_fnc = lambda x: x*(self.tri_base_points[1][1]/((self.tri_base_points[2][0]-self.tri_base_points[0][0])/3)) 

        for i in range(num_of_points):
            working_point, scalar = self.run_point()
            a = self.run_line_point()
            working_point = [working_point[0], scalar*a[1]]

            dist_to_x = working_point[1]
            z = round(random.random()*z_fnc(dist_to_x), 8)

            choice = random.random()
            if choice < 1/3:
                working_point = self.flip_over_line(self.lcomps[0], self.lcomps[1], working_point)
            elif choice < 2/3:
                working_point = self.flip_over_line(self.rcomps[0], self.rcomps[1], working_point)

            out_points[i] = [working_point[0], working_point[1], z]

        return out_points

class graph():
    def __init__(self, tri_h, num_of_points):
        """A class to automate testing"""
        self.tri_height = tri_h
        self.num_of_points = num_of_points
    
    def run(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        # points_x = np.array([[-0.5,0],[0,q],[0.5,0]])
        # points_x_sub = np.array([[-0.5,0],[0,q*(1/3)],[0.5,0]])
        tretra = randomPointInTetrahedron(1)
        graph_points = tretra.run_points(self.num_of_points)

        ax.scatter(graph_points[:, 0], graph_points[:, 1], graph_points[:, 2], color="blue", alpha=0.2)
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
