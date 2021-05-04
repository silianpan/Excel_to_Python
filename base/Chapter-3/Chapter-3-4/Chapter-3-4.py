for x in range(1,10):#循环数字1~9
    for y in range(1,10):#循环数字1~9
        txt='{0}×{1}={2}'.format(y,x,x*y)#格式化乘法表
        print(txt,end='\t')#在屏幕打印
    print()#在屏幕做换行设置




