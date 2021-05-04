#自定义平方计算函数
def square(x):
    return x**2
#调用自定义函数
print([square(n) for n in [1,2,3,4]])#使用列表推导完成每个元素的平方计算。
print(list(map(square,[1,2,3,4])))#使用map函数完成每个元素的平方计算。
