import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 11.2423512
time = np.array([11.2423512, 5.6294588, 2.8190892, 1.5492316])

speedup = smalltime / time
ax.plot([1, 2, 4, 8], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 4, 8])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Speedup", fontsize=14)
plt.grid(True)
plt.show()
