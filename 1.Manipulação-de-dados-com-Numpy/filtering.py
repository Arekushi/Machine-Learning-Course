import numpy as np

# Filtering Data
# arr = np.array([[0, 2, 3],
#                 [1, 3, -6],
#                 [-3, -2, 1]])
#
# print(f'Array: \n{arr}')
# print(f'\nArray == 3: \n{arr == 3}')
# print(f'\nArray > 0: \n{arr > 0}')
# print(f'\nArray != 1: \n{arr != 1}')
#
# # Negação do array anterior
# print(f'\nArray ~ != 1: \n{~(arr != 1)}')

# # # Is a NaN
# arr = np.array([[0, 2, np.nan],
#                 [1, np.nan, -6],
#                 [np.nan, -2, 1]])
#
# print(f'Array: \n{arr}')
# print(f'\nArray booleano verificando os NaN: \n{np.isnan(arr)}')

# Filtrando no NumPy
# print(repr(np.where([True, False, True])))
#
# arr = np.array([0, 3, 5, 3, 1])
# print(repr(np.where(arr == 3)))
#
# arr = np.array([[0, 2, 3],
#                 [1, 0, 0],
#                 [-3, 0, 0]])
# x_ind, y_ind = np.where(arr != 0)
# print(repr(np.where(arr != 0)))
# print(repr(x_ind))      # x indices of non-zero elements
# print(repr(y_ind))      # y indices of non-zero elements
# print(repr(arr[x_ind, y_ind]))

# np_filter = np.array([[True, False], [False, True]])
# positives = np.array([[1, 2], [3, 4]])
# negatives = np.array([[-2, -5], [-1, -8]])
# print(repr(np.where(np_filter, positives, negatives)))
#
# np_filter = positives > 2
# print(np_filter)
# print(repr(np.where(np_filter, positives, negatives)))
#
# np_filter = negatives > 0
# print(np_filter)
# print(repr(np.where(np_filter, positives, negatives)))

# np_filter = np.array([[True, False], [False, True]])
# positives = np.array([[1, 2], [3, 4]])
# print(repr(np.where(np_filter, positives, -1)))

# Filtragem no Eixo
# arr = np.array([[-2, -1, -3],
#                 [4, 5, -6],
#                 [3, 9, 1]])
# print(repr(arr > 0))
# print(np.any(arr > 0))
# print(np.all(arr > 0))

# arr = np.array([[-2, -1, -3],
#                 [4, 5, -6],
#                 [3, 9, 1]])
#
# print(repr(arr > 0))
# print(repr(np.any(arr > 0, axis=0)))
# print(repr(np.any(arr > 0, axis=1)))
#
# print(repr(np.all(arr > 0, axis=0)))
# print(repr(np.all(arr > 0, axis=1)))

# arr = np.array([[-2, -1, -3],
#                 [4, 5, -6],
#                 [3, 9, 1]])
#
# has_positive = np.any(arr > 0, axis=1)
# print(has_positive)
# print(repr(arr[np.where(has_positive)]))

# Time to code
def get_positives(data):
    x, y = np.where(data > 0)
    return data[x, y]


def replace_zeros(data):
    zeros = np.zeros_like(data)
    replace = np.where(data > 0, data, zeros)
    return replace


def coin_flip_filter(data):
    coin_flip = np.random.randint(2, size=data.shape)
    bool_coin_flip = coin_flip.astype(np.bool).copy()
    return np.where(bool_coin_flip, data, 1)


arr = np.array([[1, 2, 3],
                [-1, -2, -3],
                [1, 2, 3]])
print(get_positives(arr))
print(replace_zeros(arr))
print(coin_flip_filter(arr))
