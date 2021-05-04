lst=[100,57,88,66,99]#被筛选的列表。
# 使用列表推导式进行筛选。
print([n for n in lst if n>=80])
# 自定义函数与filter函数结合筛选
def fun(x):
    return x>=80
print(list(filter(fun,lst)))
# 匿名函数与filter函数结合筛选
print(list(filter(lambda x:x>=80,lst)))


