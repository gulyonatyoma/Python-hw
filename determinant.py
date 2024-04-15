import numpy as np
from time import time
import matplotlib.pyplot as plt
from itertools import *

def gauss_determinant(a: np.ndarray):
    if a.shape[0] != a.shape[1]:
        raise ValueError("matrix must be square")
    n = a.shape[0]
    if n == 1:
        return float(a[0, 0])
    ans = 1.0
    for i in range(n):
        u = i + 1
        while a[i, i] == 0:
            if u == n:
                return 0
            a[i], a[u] = a[u], a[i]
            u += 1
        for j in range(i + 1, n):
            k = a[j, i] / a[i, i]
            for g in range(i, n):
                a[j, g] -= a[i, g] * k
        ans *= a[i, i]
    return ans

def string_determinant(a: np.ndarray):
    if a.shape[0] != a.shape[1]:
        raise ValueError("matrix must be square")
    
    size = a.shape[0]
    if size == 1:
        return a[0, 0]

    ans = 0
    for j in range(size):
        bit = np.full((size, size), True)
        bit[0] = False
        bit = bit.T
        bit[j] = False 
        bit = bit.T

        ans += (-1) ** j * a[0, j] * string_det(a[bit].reshape(size - 1, size - 1))
    
    return ans


def numpy_determinant(a: np.ndarray):
    if a.shape[0] != a.shape[1]:
        raise ValueError("matrix must be squared")
    return np.linalg.det(a)

gauss_det, string_det, linal_det, x = [], [], [], []
for i in range(20):
    a = np.random.randint(-100, 100, (i, i))
    moment0 = time()
    gauss_determinant(a)
    moment1 = time()
    string_determinant(a)
    moment2 = time() 
    numpy_determinant(a)
    moment3 = time()
    gauss_det.append(moment1 - moment0)
    string_det.append(moment2 - moment1)
    linal_det.append(moment3 - moment2)
    x.append(i)
    print(i)

plt.plot(x, gauss_det, label = "gauss_det", color = "green")
plt.plot(x, string_det, label = "string_det", color = "red")
plt.plot(x, linal_det, label = "linal_det", color = "gold")
plt.grid()
plt.legend(loc = "upper left")
plt.show()