import math
import numpy as np
import matplotlib.pyplot as plt

#g = lambda x: 20 * math.sin(27 * x)
g = lambda x: -0.8
n = 10
h = 1 / n
y0 = 0
y1 = 0.2

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


def inti(func, a, b, accu):
	c = 0
	step = (b - a) / accu

	xa = a
	res = 0
	while c <= accu:
		res += func(xa)
		xa += step
		c += 1

	res -= (func(a) + func(b)) / 2
	return res * step


A = []

i = 0
while i < n - 1:
    A.append([])
    j = 0
    while j < n - 1:
        r = 0
        if i == j:
            r = 2
        elif i == j - 1 or i == j + 1:
            r = -1
        A[i].append(r)
        j = j + 1
    i = i + 1


b = []

i = 1
while i < n:
	f1 = lambda x: g(x) * (x / h + 1 - i)
	f2 = lambda x: g(x) * (-x / h + 1 + i)
	
	k = inti(f1, h * (i - 1), h * i, 200) + inti(f2, h * i, h * (i + 1), 200)
	k *= h
	b.append(k)
	i += 1

b[0] += y0
b[n - 2] += y1

nA = np.array(A)
nb = np.array(b)
ys = np.linalg.solve(nA, nb)

i = 0
#while i < n - 1:
	#print(b[i], "    ", ys[i])
	#i += 1

Y = [y0]

i = 0
while i < n - 1:
	Y.append(ys[i])
	i += 1
Y.append(y1)

X = np.arange(0, 1 + h, h)
i = 0
#while i <= n:
	#print(Y[i], "   ", X[i])
	#i += 1

dy = []
i = 0
while i < n:
	dy.append((Y[i + 1] - Y[i]) / h)
	i += 1

ff = []
i = 0
while i < n:
	ff.append((dy[i] ** 2) / 2 - g((i + 0.5) * h) * (Y[i] + Y[i + 1]) / 2)
	i += 1

print(sum(ff) * h, "    I(y)  <-- functional")

plt.plot(X, Y)

plt.xlabel('x - axis') 
plt.ylabel('y - axis') 

plt.title('FEM') 

plt.show() 