print(sorted([4,2,6])) #对列表排序。
print(sorted(('cb','a','cba'),key=len)) #对元组排序。
print(sorted({'b-10','c-8','a-14'},key=lambda x:int(x.split('-')[1]))) #对集合排序。
