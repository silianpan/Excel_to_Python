import os,openpyxl #导入库。
files=os.listdir('比赛获奖表') #获取'比赛获奖表'文件夹下的所有文件。
dic={} #初始化dic变量为空字典。
for file in files: #循环files中的工作簿名，赋值给file变量。
    wb=openpyxl.load_workbook('比赛获奖表\\'+file) #读取'比赛获奖表'文件夹下的所有工作簿。赋值给wb变量。
    for ws in wb.worksheets: #循环读取wb工作簿下的所有工作表，并赋值给ws变量。
        rows=list(ws.values)[1:] #按行获取每个工作表所有的数据，赋值给rows变量。
        for row in rows: #循环获取rows变量每行数据，并赋值给row变量。
            wbname=file.split('.')[0] #获取工作簿名称（不要扩展名），并赋值给wbname变量。
            if not wbname in dic.keys(): #如果wbnamed不存在，则进行字典键值对的新建。
                dic[wbname]=[row[2]] #在dic字典中以wbname为键，row[2]存储在列表中为值。
            else: #否则，如果wbnamed存在，则往键对应的值中添加数据。
                dic[wbname].append(row[2]) #将row[2]添加到wbname键所对应的值中。
nwb=openpyxl.Workbook() #新建工作簿。
nwb.active.append(['学区','平均分']) #在工作簿下的活动工作表中写入表头。
for key,item in dic.items(): #循环处理dic字典的所有键和值。
    nwb.active.append([key,float('{:.2f}'.format(sum(item)/len(item)))]) #key为学区，然后根据item计算平均值，将结果写工作表。
nwb.save('Chapter-12-9-1.xlsx') #保存新建的工作簿。
