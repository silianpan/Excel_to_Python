num=0 #初始化num变量为0。
for score in [98,85,93,97,88,96]: #循环列表中的数字赋值给score变量。
    if score>=90: #如果score的值大于等于90。
        num +=1 #则num变量累加1。
        if num==3: #如果num的值等于3。
            break #则退出循环。
print(score) #打印第3个大于等于90的数字97。