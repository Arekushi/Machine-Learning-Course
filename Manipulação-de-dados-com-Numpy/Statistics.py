import numpy as np

# Analysis
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# print(arr.max())
# print(arr.min())
#
# print(f"Menores de cada coluna: {arr.min(axis=0)}")
# print(f"Menores de cada linha: {arr.min(axis=1)}")
#
# print(f"Maiores de cada coluna: {arr.max(axis=0)}")
# print(f"Maiores de cada linha: {arr.max(axis=1)}")

# Métricas estatísticas
arr = np.array([[10, 20, 30],
                [4, 5, 6],
                [70, 80, 90]])
print(np.mean(arr))
print(np.var(arr))
print(np.median(arr))
print(repr(np.median(arr, axis=0)))
print(repr(np.median(arr, axis=1)))
