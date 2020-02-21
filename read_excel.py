import pandas as pd

"""
sheet_name参数
"""
# 不指定sheet_name，默认导入第一个sheet
df = pd.read_excel('./data/read_excel.xlsx')

# sheet_name参数：指定哪个工作表
# df = pd.read_excel('./data/read_excel.xlsx', sheet_name='Sheet1')

# 传入Sheet顺序，从0开始计数
# df = pd.read_excel('./data/read_excel.xlsx', sheet_name=0)

"""
指定行索引：index_col参数
默认索引为0
"""
df = pd.read_excel('./data/read_excel.xlsx', index_col=0)
print(df)

"""
指定列索引：header参数
header参数默认值为0，即默认第一行作为列索引
"""
df = pd.read_excel('./data/read_excel.xlsx', header=0)
print(df)
df = pd.read_excel('./data/read_excel.xlsx', header=1)
print(df)
df = pd.read_excel('./data/read_excel.xlsx', header=None)
print(df)