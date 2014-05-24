from plotcomplex import plot
import cmath

def plotMultI(x):
   plot.plotComplexNumbers([x, x * 1j])

#plotMultI(1 + 1j)
#plotMultI(2 - 3j)
#plotMultI(-0.5 + 7j)
#plotMultI(7 + 0.5j)

def angleBetween(z, w):
   zPolar, wPolar = cmath.polar(z), cmath.polar(w)
   return wPolar[1] - zPolar[1]


def regularAngle(a):
   while a < 0:
      a += 2*cmath.pi

   while a > 2*cmath.pi:
      a -= 2*cmath.pi

   return a


#print(regularAngle(angleBetween(1 + 1j, (1 + 1j) * 1j)))
#print(regularAngle(angleBetween(2 - 3j, (2 - 3j) * 1j)))
#print(regularAngle(angleBetween(-0.5 + 7j, (-0.5 + 7j) * 1j)))
