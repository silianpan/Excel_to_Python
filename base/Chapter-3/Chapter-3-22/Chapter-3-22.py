for num in [90,85,99,78,100]: #将列表中的数字循环赋值给num变量。
    if num<90: #如果num小于90。
        continue #则不再执行当次循环的后续语句，而直接进入下一次循环。
    txt='{}优秀'.format(num) #格式化num变量中的数字。
    print(txt) #在屏幕打印txt变量中的内容。