import numpy as np


a  = np.array([
    [4, 2, 3, 9],
    [-2, 4, 7, -7],
    [2, 3, 11, 1],
    [1, 1, 2, 0]
])

a = np.array([
    [0, -1, 1],
    [1, 1, -1],
    [-1, 0, 2]
])
def find_2by(arr):
    a = arr[0, 0] * arr[1, 1]
    b = arr[1, 0] * arr[0, 1]
    return a - b

def find_3by(arr):
    o = 0
    for i, n in enumerate(arr[0]):

        z = np.zeros((2,2))
        nc = 0

        for c in range(0,3):
            if c != i:
                z[:, nc] = arr[1:3, c]
                nc += 1

        if i%2 != 0: n = (-n)
        q = find_2by(z)
        o += n * q

    return(o)

def find_4by(arr):
    o = 0
    for i, n in enumerate(arr[0]):

        z = np.zeros((3,3))
        nc = 0
        for c in range(0,4):
            if c != i:
                z[:, nc] = arr[c, 1:4]
                nc += 1

        print(i)
        print(z)


        if i%2 != 0: n = (-n)
        q = find_3by(z)
        o += n * q

    return o
print(find_4by(a))