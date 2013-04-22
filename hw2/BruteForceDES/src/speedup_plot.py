import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 10283.2
time = np.array([10283.2, 5876.2, 4139.4, 3284.2, 2522.2, 2174.6, 2181, 2411.2, 2421, 2422.8, 2397.8, 2693.6, 2413.2, 2769.6, 2656.6, 2926.4])
speedup = smalltime / time
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Speedup", fontsize=14)
plt.grid(True)
plt.show()
