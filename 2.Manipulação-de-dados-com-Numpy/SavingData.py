import numpy as np

# Saving
arr = np.array([1, 2, 3])
np.save("saves/arr.npy", arr)

# Loading
load = np.load("saves/arr.npy")
print(load)
