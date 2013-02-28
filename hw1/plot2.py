import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 11.9414182
time = np.array([11.9989272, 6.0894932, 3.8266356, 2.4023824])

speedup = smalltime / time
ax.plot([1, 2, 4, 8], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 4, 8])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Speedup", fontsize=14)
plt.grid(True)
plt.show()
