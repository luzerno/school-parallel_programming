import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 21.87734
time = np.array([21.87734, 10.9635202, 5.4814878, 2.9210408])

speedup = smalltime / time
ax.plot([1, 2, 4, 8], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 4, 8])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Speedup", fontsize=14)
plt.grid(True)
plt.show()
