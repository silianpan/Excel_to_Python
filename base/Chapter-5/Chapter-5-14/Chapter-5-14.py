#原始列表。
lst=[85,68,98,74,95,82,93,88,74]
#使用条件列表推导。
lst1=[n for n in lst if n>=90]
print(lst1)
#使用条件循环方式。
lst2=[]
for n in lst:
    if n>=90:
        lst2.append(n)
print(lst2)