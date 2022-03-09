import numpy as np

a  = np.array([
    [4, 2, 3, 9, 19],
    [-2, 4, 7, -7, 2],
    [2, 3, 11, 1, 3],
    [1, 1, 2, 0, 2],
    [1, 1, 2, 2, 3]
])

a = np.array([
    [0, -1, 1],
    [1, 1, -1],
    [-1, 0, 2]
])

a = np.array([
    [1, 0, 2, -1],
    [3, -1, 2, 1], 
    [-2, 1, 4, -1],
    [-1, -2, 3, 1]
    ])

a = np.array([
    [-1, 0, -2, 0],
    [-3, 2, 1, -3],
    [1, -2, -1, 3], 
    [2, 1, 4, -2]
])

a = np.array([
    [17, 0, 0, 0],
    [-83, 20, 0, 0],
    [25, 100, 500, 0],
    [-6, -8, -10, 5000]
])

a = np.array([
    [1, -2, -1],
    [2, -4, 2],
    [3, -5, 1]]
)


def find_byx(arr):
    final = 0
    for i, n in enumerate(arr[0]):

        z = np.zeros((arr.shape[0] - 1, arr.shape[0] - 1))
        nc = 0
        for c in range(0,arr.shape[0]):
            if c != i:
                z[:, nc] = arr[1:arr.shape[0], c]
                nc += 1

        if z.shape[0] == 1:
            q = z[0]
            pass 

        else:
            q = find_byx(z)

        if i%2 != 0: n = (-n)
        final += n * q

    return final

def find_codeter(x,y):

    out_vec = np.zeros([1,3])

    for i in range(0,3):
        out_vec[0, i] = find_byx(np.array(
            [
                [x[i-2], y[i-2]],
                [x[1], y[i-1]]
                ]
            ))

    return(out_vec)

print(find_codeter([1,1,0],[0,1,0]))
print(find_byx(a))
