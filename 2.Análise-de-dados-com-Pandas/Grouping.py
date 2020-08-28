import pandas as pd

# Agrupamento por Coluna
# df = pd.DataFrame({
#     "yearID": [2017, 2015, 2016, 2015, 2016, 2016, 2015, 2017],
#     "teamID": ['CLE', 'CLE', 'BOS', 'DET', 'DET', 'CLE', 'BOS', 'BOS'],
#     "H": [1449, 1395, 1598, 1515, 1476, 1435, 1495, 1461],
#     "R": [818, 669, 878, 689, 750, 777, 748, 785]
# })
# print(f"Data Frame:\n{df}\n")
# groups = df.groupby('yearID')
# for year, group in groups:
#     print(f"Year: {year}")
#     print(f"Group:\n{group}\n")
#
# print(f"Group 2016:\n{groups.get_group(2016)}\n")
# print(f"Group SUM:\n{groups.sum()}\n")
# print(f"Group MEAN:\n{groups.mean()}\n")
#
# filtered = groups.filter(lambda x : x.name > 1)
# print(f"Filtered > 2015:\n{filtered}\n")

# Várias colunas
df = pd.DataFrame({
    "yearID": [2017, 2015, 2016, 2015, 2016, 2016, 2015, 2015],
    "teamID": ['CLE', 'CLE', 'BOS', 'DET', 'DET', 'CLE', 'BOS', 'BOS'],
    "H": [1449, 1395, 1598, 1515, 1476, 1435, 1495, 1461],
    "R": [818, 669, 878, 689, 750, 777, 748, 785]
})
print(f"Data Frame:\n{df}\n")

groups = df.groupby(['yearID', 'teamID'])
for name, group in groups:
    print(f"Year, Team: {name}")
    print(f"Group:\n{group}\n")

print(f"Sum:\n{groups.sum()}\n")
