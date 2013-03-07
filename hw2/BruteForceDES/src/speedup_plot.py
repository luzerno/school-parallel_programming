import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 10168.8
time = np.array([10168.8, 6770, 4770, 3724.4, 3060.2, 2716.4, 2657.6, 2593.6, 2858.4, 2924.6, 2943.8, 3010.8, 3038.8, 3024.6, 3004.6, 3063.6])
speedup = smalltime / time
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Speedup", fontsize=14)
plt.grid(True)
plt.show()
