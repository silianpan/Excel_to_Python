# 自定义函数
def counter1(iterable,min,max):#普通关键字参数。
    lst=[v for v in iterable if v>=min and v<=max]
    return len(lst)
def counter2(iterable,*,min,max):#命名关键字参数。
    lst=[v for v in iterable if v>=min and v<=max]
    return len(lst)
# 调用自定义函数
print(counter1([2,3,8,3,4,5,9],3,8)) #按位置传递实参。
print(counter1(max=8,min=3,iterable=[2,3,8,3,4,5,9])) #按关键字参数传递实参。
print(counter1([2,3,8,3,4,5,9],3,max=8)) ##部分按位置传递实参，部分按关键字参数传递实参。
print(counter2([2,3,8,3,4,5,9],3,8)) #按位置传递实参会出错。
print(counter2(max=8,min=3,iterable=[2,3,8,3,4,5,9])) #按关键字参数传递实参。
print(counter2([2,3,8,3,4,5,9],max=8,min=3))#部分按位置传递实参，部分按关键字参数传递实参。


