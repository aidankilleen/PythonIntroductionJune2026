# matplotlib_investigation.py

from matplotlib import pyplot as plt
import numpy as np

x_values = range(1, 11)
y_values = np.random.randint(1, 100, len(x_values))

plt.plot(x_values, y_values)


plt.show()