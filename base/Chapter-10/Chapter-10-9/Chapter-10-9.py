l1=[('张三',88),('李四',99),('王二',85)] #被排序的列表
l1.sort(key=lambda x:x[1],reverse=False);print(l1) #按分数升序排列。
l1.sort(key=lambda x:x[1],reverse=True);print(l1) #按分数降序排列。
