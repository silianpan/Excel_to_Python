#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 上午9:30
# @Author  : silianpan
# @Site    :
# @File    : py
# @Software: PyCharm

print(True or True)#左右两侧均为True，则返回True。
print(100==100 or 10<11)#对应案例

print(True or False)#左侧为True，右侧为False，则返回True。
print(100==100 or 10>11)#对应案例

print(False or True)#左侧为False，右侧为True，则返回True。
print(100>100 or 10<11)#对应案例

print(False or False)#左右两侧均为False，则返回False。
print(100>100 or 10>11)#对应案例