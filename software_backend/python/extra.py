import numpy as np
import random
import time
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Freq')
plt.title('Test Basic Hist')
plt.pause(0.1)
plt.show()
time.sleep(10)
print("Plot printed, resume working?")