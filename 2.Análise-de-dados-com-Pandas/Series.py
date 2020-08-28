import pandas as pd

# Dados 1-D - Series
# series = pd.Series(5)
# print(f"{series}")
#
# series = pd.Series([1, 2, 3])
# print(f"{series}")

# Index
# series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# print(f"{series}")

# Dicionário Input
# series = pd.Series({'a': 1, 'b': 2, 'c': 3})
# print(f"{series}")

# Time to Code
s1 = pd.Series([1, 2, 3])
s2 = s1 * [1, 2, 3]
print(s2)
