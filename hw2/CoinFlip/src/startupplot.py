import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
time = np.array([29.8, 50.9, 66.4, 88.6, 108.4])
ax.plot([100, 200, 300, 400, 500], time, "bo-")
ax.set_xticks(ticks=[100, 200, 300, 400, 500])
# ax.set_yticks(ticks=[0, 0.5, 1, 1.5])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Startup (ms)", fontsize=14)
plt.grid(True)
plt.show()
