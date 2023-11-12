import matplotlib.pyplot as plt
import numpy
from eanalyzer import *


# data = [[0.603125, 0.197222], [0.639063, 0.166667], [0.303125, 0.0972222], [0.628906, 0.295833], [0.290625, 0.386111], [0.417187, 0.5916665000000001], [0.6, 0.23611100000000002], [0.7375005, 0.436111], [0.39375000000000004, 0.9194445], [0.521875, 0.37916700000000003], [0.2468745, 0.691667], [0.36250000000000004, 0.4527775], [0.248437, 0.636111], [0.7164065, 0.240278], [0.6960934999999999, 0.05972225], [0.582812, 0.722222], [0.3492185, 0.116667], [0.63125, 0.426389], [0.182812, 0.155556], [0.59375, 0.6138889999999999], [0.164062, 0.655556], [0.7218745, 0.713889], [0.526563, 0.188889], [0.529688, 0.347222], [0.346875, 0.0638889], [0.5179685, 0.940278], [0.21875, 0.913889], [
#   0.32421849999999997, 0.9055555], [0.114844, 0.345833], [0.251563, 0.8], [0.792188, 0.780556], [0.484375, 0.886111], [0.5054685, 0.898611], [0.0546875, 0.4916665], [0.15, 0.2083335], [0.4656245, 0.48611150000000003], [0.301562, 0.511111], [0.34375, 0.4694445], [0.764063, 0.0111111], [0.578125, 0.3805555], [0.4375, 0.902778], [0.514063, 0.822222], [0.6828125, 0.9166665], [0.1906255, 0.891667], [0.12031249999999999, 0.486111], [0.7476565, 0.509722], [0.839844, 0.6694445], [0.7414065000000001, 0.525], [0.025, 0.369444], [0.046875, 0.261111], [0.726562, 0.566667], [0.242188, 0.602778], [0.19921850000000002, 0.42916699999999997], [0.354688, 0.736111], [0.4820315, 0.908333]]
data = [[0.603125, 0.197222], [0.639063, 0.166667], [0.303125, 0.0972222], [0.628906, 0.295833], [0.290625, 0.386111], [0.417187, 0.5916665000000001], [0.6, 0.23611100000000002], [
    0.7375005, 0.436111], [0.39375000000000004, 0.9194445], [0.521875, 0.37916700000000003], [0.2468745, 0.691667], [0.36250000000000004, 0.4527775], [0.248437, 0.636111]]

# data = [[-4, -4], [-2, -3], [-5, -1], [-2, -4],
#       [-2.5, -3], [-4.5, -2], [-4.5, -1], [-2, -1.5], [-3.5, -3], [-5, -1.25]]
print(count_rotations.count_rotations(data))

x = [row[0] for row in data]
y = [row[1] for row in data]

fig = plt.figure()
fig.add_subplot(1, 1, 1)

ax1 = plt.subplot(1, 1, 1)

ax1.plot(x, y)

plt.show()
