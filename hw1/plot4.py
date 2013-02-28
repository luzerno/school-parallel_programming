import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 22.0034534
time = np.array([22.0034534, 11.0218692, 5.5110594, 2.978827])

speedup = smalltime / time
ax.plot([1, 2, 4, 8], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 4, 8])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Speedup", fontsize=14)
plt.grid(True)
plt.show()
