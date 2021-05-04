import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-12-2-1.xlsx') #读取工作簿。
ws=wb['业绩表'] #读取工作表。
lst=list(ws.values) #按行获取ws工作表所有数据。
tit=lst[0][1:] #获取工作表首行1月到12月的数据。
num=0 #初始化num变量为0。
nws=wb.create_sheet('处理结果') #在wb工作簿中新建工作表。
for row in lst[1:]: #循环获取lst中的每个元素赋值给row变量。
    val=zip(tit,row[1:]) #使用zip函数将tit与row[1:]转换组合。
    lst1=sorted(val,key=lambda x:x[1],reverse=True) #以val每个元素的第1个元素为排序依据，进行降序排列。
    lst2=zip(*lst1) #将排序后的lst1使用zip函数再次转换组合回去。
    for v in lst2: #循环lst2变量中的元素，赋值给v变量。
        num +=1 #将num变量累加1.
        nws.append(('月份' if num%2==1 else row[0],)+v) #将各行排序后的结果写入新工作表。
wb.save('Chapter-12-2-2.xlsx') #另存工作簿。
