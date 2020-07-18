"""Plot the areas of n-polygon which have the same perimeter"""

import matplotlib.pyplot as plt
import math

__author__ = "Phuc"

def regular_polygon(perimeter, vertices):
    # Finish this function
    return 

perimeter = 4
x = []
y = []
for i in range(3,100):
    x.append(i)
    y.append(regular_polygon(perimeter, i))

plt.plot(x,y, label = "Polygon")
# plt.plot(x, [perimeter*perimeter/math.pi/4]*len(x), label = 'Circle')

plt.title(f"Areas of n-Polygon which have the same Perimeter = {perimeter}")
plt.xlabel("Number of vertices")
plt.ylabel("Area")
plt.xticks(x, fontsize = 5)
plt.yticks(y, fontsize = 5)
plt.legend()
plt.show()