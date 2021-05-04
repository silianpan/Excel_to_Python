import os,xlwt,xlrd #导入操作系统接口模块，xls读取与写入库。
files=os.listdir('销售表') #获取销售表文件夹下的所有工作簿名称。
print(files)
lst=[[file.split('.')[0],ws.name,sum(ws.col_values(1)[1:])] for file in files for ws in xlrd.open_workbook('销售表/'+file).sheets()] #对每个工作簿下每个工作表B列的数字求和。
print(lst)
lst=[['公司名','姓名','总营业额']]+lst #将表头连接到lst列表前面。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('汇总表') #新建工作簿与工作表。
row_num=0 #初始化row_num为0。
for l in lst: #循环lst列表中的每个元素。
    nws.write(row_num,0,l[0]) #将公司名写入A列。
    nws.write(row_num,1,l[1]) #将工作表名写入B列。
    nws.write(row_num,2,l[2]) #将每个人的业绩写入C列。
    row_num +=1 #累加row_num变量，并做为写入数据时的行号。
nwb.save('Chapter-5-16-1.xls') #保存工作簿。