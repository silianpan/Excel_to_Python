import xlrd #导入xlrd
from xlutils.copy import copy #导入xlutils下copy模块下的copy函数
wb=xlrd.open_workbook('Chapter-2-6-1.xls') #读取工作簿
nwb=copy(wb)#复制工作簿
ws1=nwb.get_sheet(0)#用索引号读取工作簿中的工作表
ws2=nwb.get_sheet('工资表')#用名称读取工作簿中的工作表
ws3=nwb.add_sheet('汇总表')#在工作簿中新建工作表
ws3.write(0,0,'总计')#将数据写入单元格
ws3.write(0,1,12000)#将数据写入单元格
nwb.save('Chapter-2-6-1.xls')#保存工作簿
