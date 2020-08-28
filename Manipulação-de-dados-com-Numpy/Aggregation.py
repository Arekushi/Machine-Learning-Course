import numpy as np

# Soma
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr.sum())
print(np.sum(arr))
print(arr.sum(axis=0))
print(arr.sum(axis=1))

# Soma Acumulativa
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr.cumsum())
print(arr.cumsum(axis=0))
print(arr.cumsum(axis=1))

# Concatenação
zeros = np.zeros((3, 3))
ones = np.ones((3, 3))
print(np.concatenate([zeros, ones]))
print(np.concatenate([ones, zeros]))
print(np.concatenate([zeros, ones], axis=1))
print(np.concatenate([ones, zeros], axis=1))
