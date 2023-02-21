# Plot cosine curve

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(- 2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)

plt.plot(x, y)
plt.title('Cosine graph')
plt.xlabel('Angles in radians')
plt.ylabel('Cosine value')
plt.show()