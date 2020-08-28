import pandas as pd

# Read Excel
# df = pd.read_excel("Arquivo-1.xlsx")
# print(f"Arquvo Excel:\n{df}\n")
#
# df = pd.read_excel("Arquivo-1.xlsx", sheet_name=0)
# print(f"Arquvo Excel - P1:\n{df}\n")
#
# df = pd.read_excel("Arquivo-1.xlsx", sheet_name="P2")
# print(f"Arquvo Excel - P2:\n{df}\n")
#
# df = pd.read_excel("Arquivo-1.xlsx", sheet_name=[0, 1])
# print(f"Arquvo Excel - [0, 1]:\n{df[1]}\n")
#
# df = pd.read_excel("Arquivo-1.xlsx", sheet_name=None)
# print(f"Arquvo Excel - [0, 1]:\n{df['P2']}\n")

# Read JSON
# df = pd.read_json("Arquivo-1.json")
# print(f"Arquvo JSON:\n{df}\n")
#
# df = pd.read_json("Arquivo-1.json", orient='index')
# print(f"Arquvo JSON Oriented = Index :\n{df}\n")

# Write Excel
# df1 = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
#                    'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
#
# df2 = pd.DataFrame({'c1': [10, 11, 12], 'c2': [13, 14, 15],
#                    'c3': [16, 17, 18]}, index=['r1', 'r2', 'r3'])
#
# with pd.ExcelWriter('Arquivo-1.xlsx') as writer:
#     df1.to_excel(writer, index=False, sheet_name="T1"),
#     df2.to_excel(writer, index=False, sheet_name="T2")
#
# df = pd.read_excel("Arquivo-1.xlsx", sheet_name=1)
# print(f"T2:\n{df}\n")

# Write JSON
df1 = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
df1.to_json('data2.json')

json1 = pd.read_json("data.json")
json2 = pd.read_json("data2.json")
print(f"JSON1: \n{json1}\n")
print(f"JSON2: \n{json2}\n")
