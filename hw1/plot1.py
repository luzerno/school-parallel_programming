import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
smalltime = 10.8491422
time = np.array([11.0018468, 5.5057308, 2.758659, 1.4854364, 1.5422628, 1.4817492])
speedup = smalltime / time
ax.plot([1, 2, 4, 8, 16, 32], speedup, "bo-")
ax.set_xticks(ticks=[1, 2, 4, 8, 16, 32])
plt.xlabel("Number of Threads", fontsize=14)
plt.ylabel("Speedup", fontsize=14)
plt.grid(True)
plt.show()
