import numpy as np

# Inteiros Aleatórios
print(f'Gerar um número entre 3 e 5: {np.random.randint(3, 6)}')
print(f'Gerar um número entre 3 e 5: {np.random.randint(low=3, high=6)}')

random = np.random.randint(-3, high=14, size=(2, 2))
print(f'\nArray de (2, 2) com valores entre -3 e 13: \n{random}')

# Funções Utilitárias
# # Seed
np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100, size=(2, 2))
print(f'Original seed: {random_arr}')

np.random.seed(2)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100, size=(2, 2))
print(f'New seed: {random_arr}')

np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100, size=(2, 2))
print(f'Original seed: {random_arr}')

# # Shuffle
vec = np.array([1, 2, 3, 4, 5])
print(f'Vetor: {vec}')

np.random.shuffle(vec)
print(f'Shuffle 1: {vec}')

np.random.shuffle(vec)
print(f'Shuffle 2: {vec}')

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'\nMatriz: \n{matrix}')

np.random.shuffle(matrix)
print(f'\nMatriz Shuffled: \n{matrix}')

# Distribuições
# # Distribuição Uniforme
print(np.random.uniform())
print(np.random.uniform(low=-1.5, high=2.2))
print(repr(np.random.uniform(size=3)))
print(repr(np.random.uniform(low=-3.4, high=5.9, size=(2, 2))))

# # Distribuição Normal (Gaussian)
print(np.random.normal())
print(np.random.normal(loc=1.5, scale=3.5))
print(repr(np.random.normal(loc=-2.4, scale=4.0, size=(2, 2))))

# Amostragem Personalizada
colors = np.array(['red', 'blue', 'green'])
print(f'One choice from array: {np.random.choice(colors)}')
print(f'\nChoice with size: \n{np.random.choice(colors, size=(2, 2))}')
print(f'\nChoice with size and p: \n{np.random.choice(colors, size=(2, 2), p=[0.8, 0.1, 0.1])}')
