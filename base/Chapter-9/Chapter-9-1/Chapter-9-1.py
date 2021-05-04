# 有返回值的自定义函数
def total_sum1(price,amount):
    money=price*amount
    return money
# 无返回值的自定义函数
def total_sum2(price,amount):
    str='单价:{} 数量:{} 金额:{}'.format(price,amount,price*amount)
    print(str)
# 调用自定义函数
print(total_sum1(10,20))
total_sum2(10,20)