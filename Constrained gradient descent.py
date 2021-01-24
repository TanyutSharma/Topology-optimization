import numpy as np

n = 10
maxIters = 2000
delta = 0.0001       # for finding partial derivatives
eta = 0.01           # step for gradient descent
cutoff = 10 ** (-8)  # when to stop

# The current code maximises f(x)
# Maximum is at x = [1, 1, 1, ...]
# Minimum is at x = [0, 0, 0, ...]

def f(x):
    out = 0
    for i in range(n):
        out += x[i] ** 2;
    return out

def A(p):
    Ap = np.array([[p[i] * p[j] for j in range(n)] for i in range(n)])
    Ap += np.eye(n)
    return Ap

def b(p):
    return np.ones([n])

p = np.random.rand(n) * 10
Ap = np.zeros([n, n])

norm = 1

while norm > cutoff and maxIters > 0:
    Ap = A(p)
    bp = b(p)
    
    delA = np.array([A(p + np.array([0 if i != j else delta for j in range(n)])) - Ap for i in range(n)])
    delA = delA / delta
    
     # general case
    #delB = np.array([b(p + np.array([0 if i != j else delta for j in range(n)])) - bp for i in range(n)])
    #delB = delB / delta
    delB = np.zeros([n, n]) # special case for constant b
    
    ApInv = np.linalg.inv(Ap) # Only a single inversion for each step
    
    xp = ApInv @ bp
    fx = f(xp)
    
    delF = np.array([f(xp + np.array([0 if i != j else delta for j in range(n)])) - fx for i in range(n)])
    delF = delF / delta
    
    q2 = delB - np.array([[np.sum(np.array([delA[i][k][j] * xp[i] for i in range(n)])) for j in range(n)] for k in range(n)])
    
    pGrad = delF @ (ApInv @ q2)
    
    norm = np.linalg.norm(pGrad)
    
    if maxIters % 10 == 0 :
        print(norm)
    
    p = p + (pGrad * eta)
    
    maxIters -= 1
print(norm)
print("\n\n")

print(xp)
print("Xp ^^ \n")
print(p)
print("P ^^ \n")