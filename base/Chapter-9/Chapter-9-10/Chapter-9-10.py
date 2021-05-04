# 自定义函数
def subtotals(iterable,**kwargs):
    print(kwargs)#在屏幕打印args中的内容。
    return [(key,item(iterable)) for key,item in kwargs.items()]#根据args接收的函数返回处理结果。
# 调用自定义函数
print(subtotals([7,8,9,10],求和=sum,最大=max,计数=len))