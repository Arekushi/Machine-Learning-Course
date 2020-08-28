import pandas as pd

# DataFrame
df = pd.DataFrame({
    "Nome": ["Ricardo", "Pedro", "Roberto", "Alex"],
    "Nota": [8, 9, 5, 10],
    "Aprovado": [True, True, False, True]
})

print(f"DataFrame:\n{df}\n")
# print(f"DataFrame Shape:\n{df.shape}\n")
# print(f"DataFrame Describe:\n{df.describe()}\n")
