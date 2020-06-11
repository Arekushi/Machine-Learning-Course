import numpy as np

# Ranged Data
# # Arange
arr = np.arange(5)
print(arr)

arr = np.arange(5.1)
print(arr)

arr = np.arange(0, 4)
print(arr)

arr = np.arange(-1.5, 5, 2)
print(arr)

# # Linspace
arr = np.linspace(5, 11, num=4)
print(f'Final inclusivo de 5 até 11 - {repr(arr)}')

arr = np.linspace(5, 11, num=4, endpoint=False)
print(f'Final exclusivo de 5 até 11 - {repr(arr)}')

arr = np.linspace(5, 11, num=4, dtype=np.int32)
print(f'Final inclusivo convertido para inteiro {repr(arr)}')

# Remodelando dados
# # Reshape
arr = np.arange(8)
print(arr)

reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr))
print(reshaped_arr.shape)

reshaped_arr = np.reshape(arr, (-1, 2, 2))
print(repr(reshaped_arr))
print(reshaped_arr.shape)

# # Flatten
arr = np.arange(8)
print(f'Array 1-D: {arr}')

reshaped = np.reshape(arr, (2, 4))
print(f'Array remodelado: {reshaped}')

flatten = reshaped.flatten()
print(f'Array achatado: {flatten}')

print(f'\nFormato do array 1-D: {arr.shape}')
print(f'Formato do array remodelado: {reshaped.shape}')
print(f'Formato do array achatado: {flatten.shape}')

# Transposição
# # Tranpose
arr = np.arange(8)
print(f'Array 1-D: {arr}')

reshaped = np.reshape(arr, (4, 2))
print(f'\nArray reshaped: \n{reshaped}')
print(f'Array reshaped format: {reshaped.shape}')

# arr = arr.transpose()
transposed = np.transpose(reshaped)
print(f'\nArray transposed: \n{transposed}')
print(f'Array transposed format: {transposed.shape}')

# # Tranpose with axes
arr = np.arange(24)
print(f'Array 1-D: {arr}')
print(f'Formato do array 1-D: {arr.shape}')

reshaped = np.reshape(arr, (-1, 4, 2))
print(f'\nArray remodelado:\n{reshaped}')
print(f'Formato do array remodelado: {reshaped.shape}')

transposedAxes = np.transpose(reshaped, axes=(1, 2, 0))
# Aqui ele recebe (4, 2, 3) porque -> posição 1 = 4, posição 2 = 2 e posição 0 = 3
print(f'\nArray transposed:\n{transposedAxes}')
print(f'Formato do array transposed: {transposedAxes.shape}')

# Zeros e Uns
arr = np.zeros(4)
print(f'Array de zeros: {arr}')

arr = np.ones((2, 2))
print(f'\nArray de uns:\n{arr}')

arr = np.zeros((2, 2))
print(f'\nArray de zeros:\n{arr}')

# # Criando array de zeros/uns igual a
myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'\nMeu array:\n{myArray}')
print(f'\nArray de zeros igual ao meu Array:\n{np.zeros_like(myArray)}')
