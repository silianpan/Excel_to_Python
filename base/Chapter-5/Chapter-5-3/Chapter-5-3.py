lst=[7,3,12,54,6,9,88,2,47,33,55] #要做切片处理的列表。
print(lst[2:5]) #以开头为基准切片，返回[12,54,6]。
print(lst[-9:-6]) #以结尾为基准切片，返回[12,54,6]。
print(lst[:4]) #以开头为基准切片，返回[7,3,12,54]。
print(lst[:-7])#以结尾为基准切片，返回[7,3,12,54]。
print(lst[6:]) #以开头为基准切片，返回[88,2,47,33,55]。
print(lst[-5:]) #以开头为基准切片，返回[88,2,47,33,55]。
print(lst[5:-2])#开始索引以开头为基准，结束索引以结尾为基准，返回[9,88,2,47]。
print(lst[-6:9])#开始索引以结尾为基准，结束索引以开头为基准，返回[9,88,2,47]。
print(lst[:]) #截取整个列表切片，返回[7,3,12,54,6,9,88,2,47,33,55]。
print(lst[::2]) #截取整个列表切片，步长为2，返回[7,12,6,88,47,55]。
print(lst[::-1]) #截取整个列表切片，步长为-1，返回[55,33,47,2,88,9,6,54,12,3,7]。
print(lst[::-2]) #截取整个列表切片，步长为-2，返回[55,47,88,6,12,7]。
