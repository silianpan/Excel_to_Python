#原始列表。
lst=[[1,2],[3,4,5],[6,7]]
#使用嵌套列表推导。
lst1=[v*10 for l in lst for v in l]
print(lst1)
#使用嵌套循环方式。
lst2=[]
for l in lst:
    for v in l:
        lst2.append(v*10)
print(lst2)