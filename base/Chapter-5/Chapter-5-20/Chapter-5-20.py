l=[['a','b','c'],[1,2,3]] #提供要重新组合的列表。
lst1=list(zip(l[0],l[1])) #将要转换的值分别放到zip的不同参数位置。
print(lst1) #在屏幕打印重新组合后lst1的结果。
lst2=list(zip(*l)) #直接将整个l列表放到zip中。
print(lst2) #在屏幕打印重新组合后lst2的结果。
lst3=list(zip(*lst2)) #再组合回原来的结构。
print(lst3) #在屏幕打印重新组合后lst3的结果。
print(list(zip(iter([1,2,3]))))


