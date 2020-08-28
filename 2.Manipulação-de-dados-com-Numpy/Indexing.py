import numpy as np

# Array accessing
arr = np.array([1, 2, 3, 4, 5])
print(f'Array: {arr}')
print(f'Posição 0 do array: {arr[0]}')
print(f'Posição 4 do array: {arr[4]}')

arr = np.array([[6, 3], [0, 2]])
print(f'\nMatriz: \n{arr}')
print(f'Posição 0 da matriz: {arr[0]}')
print(f'Posição 0 e 1 da matriz: {arr[0][1]}')

# Slicing
# # Array
arr = np.array([0, 1, 2, 3, 4])
print(arr[:])

print(f'Positive: {arr[1:]}')
print(f'Negative: {arr[-4:]}')

print(f'Positive: {arr[2:4]}')
print(f'Negative: {arr[-3:-1]}')

print(f'Positive: {arr[:4]}')
print(f'Negative: {arr[:-1]}')

print(f'Positive: {arr[3:]}')
print(f'Negative: {arr[-2:]}')

# # Matriz
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(f'\nQualquer linha: \n{arr[:]}')
print(f'\nDa linha 1 em diante: \n{arr[1:]}')
print(f'\nQualquer linha e apenas a coluna 2: \n{arr[:, -1]}')
print(f'\nQualquer linha e apenas da coluna 1 em diante: \n{arr[:, 1:]}')
print(f'\nDa linha 0 até a 2 e apenas da coluna 1 em diante: \n{arr[0:2, 1:]}')
print(f'\nApenas linha 0 e da coluna 1 em diante: \n{arr[0, 1:]}')

# Argmin and Argmax
# # Retorna o index do menor e maior número
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])

print(f'Array: \n{arr}')
print(f'\nIndex do menor item da linha 0: {np.argmin(arr[0])}')
print(f'Index do maior item da linha 0: {np.argmax(arr[0])}')

print(f'Index do menor item da linha 2: {np.argmin(arr[2])}')
print(f'Index do maior item da linha 2: {np.argmax(arr[2])}')

print(f'Index do menor item do array inteiro: {np.argmin(arr)}')
print(f'Index do menor item do array inteiro: {np.argmax(arr)}')

# # With axis argument
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])

print(f'Array: \n{arr}')
print(f'\nArgmin axis 0: {np.argmin(arr, axis=0)}')  # Elemento mínimo da linha para coluna (-3, -1, -6)
print(f'Argmin axis 1: {np.argmin(arr, axis=1)}')  # Elemento mínimo da coluna para linha (-3, -6, -3)

print(f'\nArgmax axis 0: {np.argmax(arr, axis=0)}')  # Elemento máximo da linha para coluna (4, 9, 1)
print(f'Argmax axis 1: {np.argmax(arr, axis=1)}')  # Elemento máximo da coluna para linha (-1, 5, 9)


# Time to code!
def slice_data(data):
    slice1 = data[:, 1:]
    slice2 = data[0:3, :-2]
    return slice1, slice2


arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
print(slice_data(arr))
