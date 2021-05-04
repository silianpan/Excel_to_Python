#原始列表
lst=[[1,2,5],[10,5,6],[8,5,3]]
#列表推导式1
lst1=[l[0]*l[1]*l[2] for l in lst]
print(lst1)
#列表推导式2
lst2=[x*y*z for x,y,z in lst]
print(lst2)
#循环方式1
lst3=[]
for l in lst:
    lst3 +=[l[0]*l[1]*l[2]]
print(lst3)
#循环方式2
lst4=[]
for x,y,z in lst:
    lst4 +=[x*y*z]
print(lst4)
