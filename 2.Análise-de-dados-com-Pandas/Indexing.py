import pandas as pd

# Col
# df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
#                    'c3': [5, 6]}, index=['r1', 'r2'])
# print(f"DataFrame:\n{df}\n")
#
# c1 = df['c1']
# print(f"C1:\n{c1}\n")
#
# c1_df = df[['c1']]
# print(f"C1_DF:\n{c1_df}\n")
#
# c23 = df[['c2', 'c3']]
# print(f"C23:\n{c23}\n")

# Row
# df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
#                    'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
# print(f"DataFrame:\n{df}\n")
#
# first = df[:1]
# print(f"First:\n{first}\n")
#
# firstTwo = df[:2]
# print(f"First and Two:\n{firstTwo}\n")
#
# r2r3 = df["r2":"r3"]
# print(f"R2 and R3:\n{r2r3}\n")

# Other Indexing iloc
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
print(f"DataFrame:\n{df}\n")

iloc = df.iloc[0]
print(f"Iloc [1]:\n{iloc}\n")

iloc = df.iloc[0, 2]
print(f"Iloc [0, 2]:\n{iloc}\n")

iloc = df.iloc[[True, False, True]]
print(f"Iloc [T, F, T]:\n{iloc}\n")

# Loc
df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
print(f"DataFrame:\n{df}\n")

loc = df.loc['r2']
print(f"Loc R2:\n{loc}\n")

loc = df.loc[[True, False, True]]
print(f"Loc [T, F, T]:\n{loc}\n")

loc = df.loc['r2', 'c2']
print(f"Loc [r2, c2]:\n{loc}\n")

loc = df.loc[['r1', 'r2'], 'c2']
print(f"Loc [r1, r2], c2:\n{loc}\n")
