import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

from . import xkcdify

def complexRanges(numbers):
   reals = [x.real for x in numbers]
   clxs = [x.imag for x in numbers]

   return (min(reals), max(reals)), (min(clxs), max(clxs))


# plotComplexNumbers : [complex] -> None
# display a plot of the given list of complex numbers
# window manually sets the plot window ((xMin, xMax), (yMin, yMax))
def plotComplexNumbers(numbers, window=None):
   plt.clf()
   ax = plt.subplot(111)

   if window is None:
      realRange, clxRange = complexRanges(numbers)
      lbound = lambda x: x - 0.2*abs(x)
      ubound = lambda x: x + 0.2*abs(x)

      xMin, xMax = lbound(realRange[0]), ubound(realRange[1])
      yMin, yMax = lbound(clxRange[0]), ubound(clxRange[1])

      xMin = min(-0.5, xMin)
      yMin = min(-0.5, yMin)
      xMax = max(0.5, xMax)
      yMax = max(0.5, yMax)
   else:
      ((xMin, xMax), (yMin, yMax)) = window

   ax.set_xlim([xMin, xMax])
   ax.set_ylim([yMin, yMax])

   for number in numbers:
      ax.annotate("",
                  xy=(number.real, number.imag), xycoords='data',
                  xytext=(0, 0), textcoords='data',
                  arrowprops=dict(arrowstyle="->",
                                  connectionstyle="arc3",
                                 lw=2),
                  )
      halign = 'left' if number.real > 0 else 'right'
      valign = 'bottom' if number.real > 0 else 'top'
      ax.text(number.real, number.imag, str(number), horizontalalignment=halign, verticalalignment=valign)

   #XKCDify the axes -- this operates in-place
   xkcdify.XKCDify(ax, xaxis_loc=0, yaxis_loc=0, xaxis_arrow='',
         yaxis_arrow='', expand_axes=True, mag=0.0)

   plt.show()



def gridToImage(grid):
   plt.clf()
   plt.imshow(grid)
   plt.set_cmap('hot')
   plt.show()



if __name__ == "__main__":
   plotComplexNumbers([(-1+1j), (1+2j), (-1.5 - 0.5j), (.6 - 1.8j)])
