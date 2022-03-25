from operator import index
from matplotlib import pyplot as plt
import numpy as np
import random

NUM_OF_POINTS = 1000
arr = np.random.rand(NUM_OF_POINTS,2)
print(arr.shape)


fnc = lambda a: True if a.sum() < 1 else False
arr_sum = arr.sum(1)

indexes = np.nonzero(arr_sum > 1)
arr = arr[indexes] 
print(arr.shape)

plt.scatter(arr[:, 0], arr[:, 1])
plt.show()