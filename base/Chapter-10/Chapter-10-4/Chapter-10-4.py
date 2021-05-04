print([a+b for a,b in zip([1,2],[10,20])])#使用列表推导将完成两列表相加，方法1。
print([(lambda x,y:x+y)(a,b) for a,b in zip([1,2],[10,20])])#使用列表推导将完成两列表相加，方法2。
print(list(map(lambda x,y:x+y,[1,2],[10,20])))#使用map函数完成两列表相加。