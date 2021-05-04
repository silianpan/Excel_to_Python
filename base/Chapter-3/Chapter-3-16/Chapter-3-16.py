lst=[69,89,95,54] #循环要判断的数字。
for num in lst: #将lst列表中的值赋值给num变量。
    if num>=90: #当num大于等于90。
        print(num,'优') #则在屏幕打印'优'。
    elif num>=80: #当num大于等于80。
        print(num,'良') #则在屏幕打印'良'。
    elif num>=60: #当num大于等于60。
        print(num,'中') #则在屏幕打印'中'。
    else: #上面的所有条件均不成立时。
        print(num,'差') #则在屏幕打印'差'。