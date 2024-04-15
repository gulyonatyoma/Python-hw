import numpy as np 

def spiral_filling(r: int, c: int) -> np.ndarray:
    ret = np.zeros((r, c))
    
    top = 0
    bottom = r - 1
    left = 0
    right = c - 1
    ind = 1
    while True:
        if left > right:
            break
        for i in range(left, right + 1):
            ret[top][i] = ind 
            ind += 1
        top += 1
        if top > bottom:
            break
        for i in range(top, bottom + 1):
            ret[i][right] = ind 
            ind += 1
        right -= 1
        if left > right:
            break
        for i in range(right, left - 1, -1):
            ret[bottom][i] = ind
            ind += 1
        bottom -= 1
        if top > bottom:
            break
        for i in range(bottom, top - 1, -1):
            ret[i][left] = ind 
            ind += 1
        left += 1
    return ret