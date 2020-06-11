import numpy as np

# Entender álgebra aritmética e linear
# Aritmética
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f'Array: \n{arr}')
print(f'\narr + 1\n{arr + 1}')        # Adicionando mais 1 para cada elemento
print(f'\narr - 1.2\n{arr - 1.2}')      # Adicionando menos 1.2 para cada elemento
print(f'\narr * 2\n{arr * 2}')        # Adicionando multiplicando em 2 para cada elemento
print(f'\narr / 2\n{arr / 2}')        # Adicionando dividindo em 2 para cada elemento
print(f'\narr // 2\n{arr // 2}')       # Adicionando dividindo em 2 e retornando um inteiro para cada elemento
print(f'\narr ** 2\n{arr ** 2}')       # Adicionando cada elemento elevado em 2

# Non-Linear Functions
# # Exponenciais e Logaritmos
arr = np.array([[1, 2], [3, 4]])
print(f'Array: \n{arr}')
print(f'\nArray exp: \n{np.exp(arr)}')
print(f'\nArray exp base 2 (exp2): \n{np.exp2(arr)}')

arr2 = np.array([[1, 10], [np.e, np.pi]])
print(f'\nArray2: \n{arr2}')
print(f'\nArray de log: \n{np.log(arr2)}')
print(f'\nArray de log base 10: \n{np.log10(arr2)}')

# # Potência
arr3 = np.array([[1, 2], [3, 4]])
# 2 ^ 1; 2 ^ 2; 2 ^ 3; 2 ^ 4
print(f'Base 2: \n{np.power(2, arr3)}')

# 1 ^ 2; 2 ^ 2; 3 ^ 2; 4 ^ 2
print(f'\nBase arr3: \n{np.power(arr3, 2)}')

arr4 = np.array([[10.2, 4], [3, 5]])
# 10.2 ^ 1; 4 ^ 2; 3 ^ 3; 5 ^ 4
print(f'\n Base arr4: \n{np.power(arr4, arr3)}')

# Multiplicação de Matrizes
arr1 = np.array([1, 2, 3])
arr2 = np.array([-3, 0, 10])
print(f'Produto escalar: {np.matmul(arr1, arr2)}')

arr3 = np.array([[1, 2], [3, 4], [5, 6]])   # (3, 2)
arr4 = np.array([[-1, 0, 1], [3, 2, -4]])   # (2, 3)

# # Resulta em um array de (3, 3)
print(f'\n arr3 * arr4: \n{np.matmul(arr3, arr4)}')

# # Resulta em um array de (2, 2)
print(f'\n arr4 * arr3: \n{np.matmul(arr4, arr3)}')
