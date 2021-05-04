num=0 #初始化num变量。
while num<6: #判断当num小于6。
    num +=1 #则对num变量累加1。
    if num%2==0: #判断当num除以2的余数为0。
        continue #则跳出本次循环，进入下一次循环。
    print(num) #在屏幕打印累加出来的数字。