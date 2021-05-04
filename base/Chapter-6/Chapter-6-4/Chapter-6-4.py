tup=(1,2,3) #被循环的元组。
tup1=(t*10 for t in tup) #元组推导式。
print(tup1) #在屏幕打印tup1元组。
print(tuple(tup1)) #将tup1迭代器转换为元组。

tup2=() #创建空元组。
for t in tup: #循环tup元组的元素。
    tup2 +=(t*10,) #将tup中的元素乘以10，再积累合并到tup2变量。
print(tup2) #在屏幕打印tup2元组。
