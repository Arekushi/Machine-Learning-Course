import pandas as pd

df = pd.DataFrame({
  'T1': [10, 15, 8],
  'T2': [25, 27, 25],
  'T3': [16, 15, 10]})

print(f"DataFrame:\n{df}\n")
print(f"DataFrame SUM:\n{df.sum()}\n")
print(f"DataFrame SUM AXIS=1:\n{df.sum(axis=1)}\n")

# Recursos ponderados
df = pd.DataFrame({
    'T1': [0.1, 150],
    'T2': [0.25, 240],
    'T3': [0.16, 100]})

print(f"DataFrama:\n{df}\n")
print(f"DataFrame multiplicado por 2:\n{df.multiply(2)}\n")

print(f"DataFrame multiplicado por 1000 (linha 0) e por 2 (linha 1)\n{df.multiply([1000, 2], axis=0)}\n")
print(f"DataFrame multiplicando as três colunas pelos valores da lista:\n{df.multiply([2, 0.5, 2])}\n")
