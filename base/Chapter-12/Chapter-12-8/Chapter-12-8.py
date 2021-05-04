import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-12-8-1.xlsx')#读取工作簿。
ws=wb['分数表']#读取工作表。
dic={} #初始化dic变量为空字典。
nwb=openpyxl.Workbook()#新建工作簿。
nwb.active.append(['校名','年级','班级','总分','人数'])#在新工作簿下的默认创建的新工作表中写入表头。
for row in list(ws.values)[1:]:#按行获取ws工作表的所有数据，并按行循环给row变量。
    if not row[:3] in dic.keys():#以校名、年纪、班级构成的元组做字典的键，判断在dic字典中是否存在，如果不存在。
        dic[row[:3]]=[row[-1]]#则(校名,年纪,班级)为键，分数为值，新建键值对。
    else:#否则，如果条件成立。
        dic[row[:3]].append(row[-1])#则向键对应的值添加元素。
for key,item in dic.items():#循环dic字典中的所有键和值。对应赋值给key和item变量。
    nwb.active.append(key+(sum(item),len(item)))#将字典中的键与求和、计数结果合并成元组，再写入新工作表。
nwb.save('Chapter-12-8-2.xlsx') #保存新建的工作簿。
