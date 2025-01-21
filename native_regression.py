
import sys
import matplotlib.pyplot as plt
from matrix import *

X, Y = transpose(loadtxt(sys.argv[1]))

Xp = powers(X,0,1)
Yp = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

def f(x): return b + m*x

Y2 = list(map(f,X))

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()