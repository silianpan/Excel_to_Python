import copy #导入复制模块。
tup1=(1,2,3) #准备要复制的元组。
tup2=copy.copy(tup1) #将浅复制tup1元组，并赋值给tup2变量。
tup3=copy.deepcopy(tup1)#将深复制tup1元组，并赋值给tup3变量。
print(id(tup1),id(tup2),id(tup3)) #在屏幕打印tup1、tup2、tup3元组的内存地址。

tup4=(1,[2],3) #准备要复制的元组。
tup5=copy.copy(tup4) #将浅复制tup4元组，并赋值给tup5变量。
tup6=copy.deepcopy(tup4) #将深复制tup4元组，并赋值给tup6变量。
print(id(tup4),id(tup5),id(tup6)) #在屏幕打印tup4、tup5、tup6元组的内存地址。

