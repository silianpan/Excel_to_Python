# 原始列表。
lst=['89','96','100','72']
#使用列表推导。
lst1=[int(n) for n in lst]
print(lst1)
#使用循环方式。
lst2=[]
for n in lst:
    lst2.append(int(n))
print(lst2)