import numpy as np


a  = np.array([
    [4, 2, 3, 9],
    [-2, 4, 7, -7],
    [2, 3, 11, 1],
    [1, 1, 2, 0]
])

# a = np.array([
#     [1, 2, 4],
#     [1, 2, 1],
#     [1, -.5, 1]
# ])

def find_byx(arr):
    final = 0
    for i, n in enumerate(arr[0]):

        z = np.zeros((arr.shape[0] - 1, arr.shape[0] - 1))
        nc = 0
        for c in range(0,arr.shape[0]):
            if c != i:
                z[:, nc] = arr[1:arr.shape[0], c]
                nc += 1

        if z.shape[0] == 2:
            a = z[0, 0] * z[1, 1]
            b = z[1, 0] * z[0, 1]
            q =  a - b

        else:
            q = find_byx(z)

        if i%2 != 0: n = (-n)
        final += n * q

    return final

3d
print(find_byx(a))