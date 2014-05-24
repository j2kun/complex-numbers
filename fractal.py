from plotcomplex.plot import gridToImage

def squarePlusOne(z):
   return z*z + 1

def squareMinusOne(z):
   return z*z - 1

def squarePlusC(c):
   def f(z):
      return z*z + c

   return f

def isSmallForever(z, f):
   k = 0

   while abs(z) < 2:
      z = f(z)
      k += 1

      if k > 250:
         return True

   return False


def frange(start, stop, step):
   while start < stop:
      yield start
      start += step


def classify(classifier, xRange=(-2,2), yRange=(-2,2), step=0.1):
   xStart, xEnd = xRange
   yStart, yEnd = yRange
   xSize = int((xEnd - xStart) / step)
   ySize = int((yEnd - yStart) / step)

   grid = [[0 for j in range(xSize)] for i in range(ySize)]

   for i in range(ySize):
      b = yEnd - i * step

      for j in range(xSize):
         a = xStart + j * step
         z = a + b * 1j
         if classifier(z):
            grid[i][j] = 1

   return grid


if __name__ == "__main__":
   def classifySquarePlusOne(z):
      return isSmallForever(z, squarePlusOne)

   def classifySquareMinusOne(z):
      return isSmallForever(z, squareMinusOne)

   #grid = classify(classifySquarePlusOne)
   #gridToImage(grid)
   #grid = classify(classifySquareMinusOne, step=0.001)
   #gridToImage(grid)

   def classifySquarePlusC(c):
      return isSmallForever(0, squarePlusC(c))

   grid = classify(classifySquarePlusC, xRange=(-2,1), yRange=(-1,1), step=0.001)
   #grid = classify(classifySquarePlusC, xRange=(0.1,0.2), yRange=(0.55,0.7), step=0.0001)
   gridToImage(grid)
