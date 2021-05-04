txt='Python与Excel' #要做切片处理的字符串。
print(txt[2:9]) #以开头为基准切片，返回值为'thon与Ex'。
print(txt[-10:-3])#以结尾为基准切片，返回值为'thon与Ex'。
print(txt[:7]) #以开头为基准切片，返回值为'Python与'。
print(txt[:-5])#以结尾为基准切片，返回值为'Python与'。
print(txt[7:]) #以开头为基准切片，返回值为'Excel'。
print(txt[-5:])#以开头为基准切片，返回值为'Excel'。
print(txt[2:-5])#开始索引以开头为基准，结束索引以结尾为基准，返回'thon与'。
print(txt[-10:7])#开始索引以结尾为基准，结束索引以开头为基准，返回'thon与'。
print(txt[:])#截取整个字符串切片，返回值为'Python与Excel'。
print(txt[::2])#截取整个字符串切片，步长为2，返回值为'Pto与xe'。
print(txt[::-1])#截取整个字符串切片，步长为-1，返回值为'lecxE与nohtyP'。
print(txt[::-2])#截取整个字符串切片，步长为-2，返回值为'lcEnhy'。