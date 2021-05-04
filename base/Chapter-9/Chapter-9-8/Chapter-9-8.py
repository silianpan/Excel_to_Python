# 自定义combine函数。
def combine(range,join_range,delimiter=' '):
    dic={}#初始化dic变量为空字典。
    for x,y in zip(range,join_range):#将range和join_range接收的值使用zip函数做组合转换，并赋值给x,y变量。
        if not x in dic:#如果x在dic字典中不存在。
            dic[x]=[y]#则以x为键，y为值，创建键值，注意y是写在列表中的。
        else:#否则。
            dic[x].append(y)#如果x键存在，则将y添加到对应的值列表中。
    l=[(k,delimiter.join([str(i) for i in dict.fromkeys(i)])) for k,i in dic.items()]#将键对应值列表去重合并。
    return l#l变量是列表，列表中的元素是元组类型，元组中分别存储是dic字典的键，及dic字典对应值合并后的字符串。
# 自定义函数应用
import xlrd #导入xls文件读取库。
from xlutils.copy import copy #导计工作簿复制函数。
wb=xlrd.open_workbook('Chapter-9-8-1.xls');ws=wb.sheet_by_name('工资表') #读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('结果表') #复制工作簿，以及读取副本工作簿下的工作表。
row_num=0#初始化row_num变量为。
for x,y in combine(delimiter='、',range=ws.col_values(0),join_range=ws.col_values(2)):#调用combine函数。
    nws.write(row_num,0,x)#将range参数中的值去重后写入'结果表'工作表A列。
    nws.write(row_num,1,y)#将join_range参数中的值去重合并再写入'结果表'工作表B列。
    row_num +=1#累加row_num变量。
nwb.save('Chapter-9-8-1.xls')#保存副本工作簿。