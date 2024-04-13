import numpy as np

def ldu(a: np.ndarray) -> tuple[np.ndarray]:
    n = a.shape[0]
    l = np.zeros((n, n))
    d = np.zeros((n, n))
    u = np.zeros((n, n))
    for i in range(n - 1):
        for j in range(i + 1, n):
            l[j, i] = a[j, i]
    for i in range(n):
        d[i, i] = a[i, i]
    for i in range(n - 1):
        for j in range(i + 1, n):
            u[i, j] = a[i, j]
    return l, d, u

a = np.array([[9, -1, 9, 6], [6, 1, -4, -4], [-7, 5, 1, 3], [-8, 1, -3, -5]])

print(*ldu(a))

