print([(lambda x:x**2)(n) for n in [1,2,3,4]])#使用列表推导完成每个元素的平方计算。
print(list(map(lambda x:x**2,[1,2,3,4])))#使用map函数完成每个元素的平方计算。