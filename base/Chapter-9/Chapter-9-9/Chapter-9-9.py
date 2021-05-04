# 自定义函数
def subtotal(iterable,*args):
    print(args)#在屏幕打印args中的内容。
    return [fun(iterable) for fun in args]#根据args接收的函数返回处理结果。
# 调用自定义函数
print(subtotal([7,8,9,10],max,min,sum))