import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 10283.2
time = np.array([10283.2, 12540.6, 12995.8, 16283.2, 36958])
speedup = smalltime / time
ax.plot([1, 2, 4, 8, 16], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 4, 8, 16])
ax.set_yticks(ticks=[0, 0.5, 1, 1.5])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Scaleup", fontsize=14)
plt.grid(True)
plt.show()
