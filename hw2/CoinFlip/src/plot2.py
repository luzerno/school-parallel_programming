import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 18251.2
time = np.array([18251.2, 18264.4, 18269.4, 18273.2, 18313.8, 18320.2, 18391, 19951.2, 23660, 25453.2, 28029.8, 30312.8, 32495.8, 35042.4, 37173.4, 39671.2])
speedup = smalltime / time
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
ax.set_yticks(ticks=[0, 0.5, 1, 1.5])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Scaleup", fontsize=14)
plt.grid(True)
plt.show()
