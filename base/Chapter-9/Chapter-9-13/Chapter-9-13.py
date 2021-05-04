fun1=lambda x,y:x+y #必选参数的匿名函数。
print(fun1(10,20)) #调用fun1函数。
fun2=lambda x,y=20:x+y #可选参数的匿名函数。
print(fun2(10)) #调用fun2函数。
fun3=lambda l,*fun:[f(l) for f in fun] #不定长参数的匿名函数1。
print(fun3([3,4,5],sum,max,min)) #调用fun3函数。
fun4=lambda l,**fun:[k+':'+str(i(l)) for k,i in fun.items()] #不定长参数的匿名函数2。
print(fun4([3,4,5],求和=sum,最大=max,最小=min)) #调用fun4函数。
