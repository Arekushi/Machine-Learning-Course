import pandas as pd

# DataFrame
# df = pd.DataFrame()
# print(f"{df}\n")
#
# df = pd.DataFrame([5, 6])
# print(f"{df}\n")
#
# df = pd.DataFrame([[5, 6]])
# print(f"{df}\n")
#
# df = pd.DataFrame([[5, 6], [1, 3]])
# print(f"{df}\n")
#
# df = pd.DataFrame([[5, 6], [1, 3]], index=['r1', 'r2'], columns=['c1', 'c2'])
# print(f"{df}\n")
#
# df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]}, index=['r1', 'r2'])
# print(f"{df}\n")

# Upcasting
# df = pd.DataFrame([[1, 2], [3.5, 4]])
# print(f"{df}\n")

# Anexando Linhas
# df = pd.DataFrame([[1, 2], [3.5, 4]])
# print(f"{df}\n")
#
# ser = pd.Series([0, 0], name='r3')
# newDf = df.append(ser)
# print(f"{newDf}\n")
#
# newDf = df.append(ser, ignore_index=True)
# print(f"{newDf}\n")
#
# otherDf = pd.DataFrame([[9, 9], [8, 8]])
# newDf = df.append(otherDf, ignore_index=False)
# print(f"{newDf}\n")
#
# otherDf = pd.DataFrame([[9, 9], [8, 8]])
# newDf = df.append(otherDf, ignore_index=True)
# print(f"{newDf}\n")

# Droping Data
# df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
# print(f"{df}\n")
#
# drop_df = df.drop(labels='r1')
# print(f"{drop_df}\n")
#
# drop_df = df.drop(columns='c1')
# print(f"{drop_df}\n")
#
# drop_df = df.drop(columns=['c1', 'c2'])
# print(f"{drop_df}\n")
