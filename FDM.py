import math
import matplotlib.pyplot as plt
import numpy as np

n = 20
y0, y1 = 0, 0.1
h = 1 / n
g = lambda x: math.sin(7 * x)

def matP(mat):
    s = ""
    i = 0
    while i < len(mat):
        j = 0
        s = s + "["
        while j < len(mat[0]):
            s = s + str(round(mat[i][j], 3)) + ", "
            j = j + 1
        s = s + "]\n"
        i = i + 1
    print(s)


def take(ri, rf, mat, fac):
    i = 0
    while i < len(mat) + 1:
        mat[rf][i] = mat[rf][i] - mat[ri][i] * fac
        i = i + 1
    


def ccol(r, c, mat):
    j = 0
    while j < len(mat):
        if j != r:
            take(r, j, mat, mat[j][c] / mat[r][c])
        j = j + 1
    

def solve(n, g, ua, ub):
    mat = []
    ret = []
    
    i = 0
    while i < n - 1:
        mat.append([])
        j = 0
        while j < n:
            r = 0
            if i == j:
                r = 2
            elif i == j - 1 or i == j + 1:
                r = -1
            if j == n - 1:
                r = g((i + 1) / n)
            mat[i].append(r)
            j = j + 1
        i = i + 1
    
    mat[0][n - 1] = mat[0][n - 1] + ua * n * n
    mat[n - 2][n - 1] = mat[n - 2][n - 1] + ub * n * n
    #matP(mat)
    i = 0
    while i < n - 1:
        ccol(i, i, mat)
        i = i + 1
    #matP(mat)
    i = 0
    while i < n - 1:
        ret.append((mat[i][n - 1] / mat[i][i]) / (n * n))
        i = i + 1

    return ret

ys = solve(n, g, y0, y1)

Y = [y0]

i = 0
while i < n - 1:
    Y.append(float(ys[i]))
    i += 1
Y.append(y1)

X = np.arange(0, 1 + h, h)

plt.plot(X, Y)

plt.xlabel('x - axis') 
plt.ylabel('y - axis') 

plt.title('FDM') 

plt.show() 