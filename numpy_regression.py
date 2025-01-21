
import sys
import matplotlib.pyplot as plt
from numpy import *

STEP = 0.2


def powers(num_list, min, max):
    rM = []
    for idx, num in enumerate(num_list):
        rM.append(list())
        for power in range(min, max+1):
            rM[idx].append(num**power)
    return array(rM)


X, Y = transpose(loadtxt(sys.argv[1]))
regpow = int(sys.argv[2])
Xp = powers(X,0,regpow)
Yp = powers(Y,1,1)
Xpt = transpose(Xp)


A = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))

def poly(A, x): return sum([a*x**pow for pow, a in enumerate(A)])
def f(x): return poly(A, x)

X2 = linspace(min(X), max(X), int(len(X)/STEP)).tolist()
Y2 = list(map(f,X2))

plt.plot(X,Y,'ro')
plt.plot(X2,Y2)
plt.show()