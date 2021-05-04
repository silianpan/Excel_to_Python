lst=[95,89,69,100,88,94,91]#要被循环判断的数字列表。
counter_a,counter_b=0,0#分别初始化counter_a和counter_b变量值为0。
for num in lst:#循环lst变量中的数字。
    if num>=90:#如果num大于等于90。
        counter_a +=1#条件成立则将计数到counter_a变量中。
    else:#如果num不大于等于90。
        counter_b +=1#条件不成立则将计数到counter_b变量中。
print('>=90有{}个，<90有{}个。'.format(counter_a,counter_b))#统计>=90与<90的数字个数。