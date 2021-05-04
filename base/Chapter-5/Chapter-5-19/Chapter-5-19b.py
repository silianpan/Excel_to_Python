#列表中元素是单值。
import copy #导入复制模块。
lst1=[1,2,3,4]#准备要被复制的列表。
lst2=copy.deepcopy(lst1)#使用复制模块下的深复制方法来复制lst1，并赋值给lst2。
lst1[3]=100#修改lst1中的元素。也可以修改lst2中的元素。
print(lst1,lst2)#对深复制前、后两个列表的数据。
#列表中元素是容器型元素
lst3=[1,[2,3],4]#准备要被复制的列表。
lst4=copy.deepcopy(lst3)#使用复制模块下的深复制方法来复制lst3，并赋值给lst4。
lst3[1][0]=100#修改lst3中的元素。也可以修改lst4中的元素。
print(lst3,lst4)#对深复制前、后两个列表的数据。



