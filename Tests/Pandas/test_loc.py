import pandas as pd

df = pd.DataFrame({
    "Nome": ["Ricardo", "Pedro", "Roberto", "Alex"],
    "Nota": [8, 9, 5, 10],
    "Aprovado": [True, True, False, True]
})

# Definindo LOC e ILOC
# LOC se basea em rótulos - labels
# ILOC se basea nos índices (números inteiros)

# Filtrando
print(f"Filtrando usando o nome:\n{df[df['Nome'] == 'Pedro']}\n")

# Filtrando pela chave (key)
print(f"Filtrando pela chave (key) - Nome, Nota:\n{df[['Nome', 'Nota']]}\n")

# Filtrando pelas linhas
print(f"Filtrando pelas linhas - 0 : 2:\n{df[0:2]}\n")

# LOC
print(f"Filtando (loc) - Linha 0:\n{df.loc[[0]]}\n")
print(f"Filtando (loc) - Linha 0 e 3:\n{df.loc[[0, 3]]}\n")
print(f"Filtando (loc) - Todas as linhas:\n{df.loc[:]}\n")
print(f"Filtando (loc) - Linha 0 até 2, Todos antes de \'Nota\':\n{df.loc[:2, :'Nota']}\n")
print(f"Filtando (loc) - Linha 0\nApenas com as colunas que queremos:\n{df.loc[[0], ['Nome', 'Nota']]}\n")

# LOC com operadores lógicos
print(f"Filtando usando LOC com operadores lógicos - Nota > 5:\n{df.loc[df['Nota'] > 5]}\n")

# ILOC
print(f"Filtando (iloc) Linha 0 até 3:\n{df.iloc[:3]}\n")
print(f"Filtando (iloc) Linha 0 até 3 e Coluna 0 até 2:\n{df.iloc[:3, :2]}\n")
