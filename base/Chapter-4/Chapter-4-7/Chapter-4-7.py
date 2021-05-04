txt='张三19,李四,张三9,林林6,张三12,张三8'#被查找的字符串。
print(txt.index('张三'))#返回值为0。
print(txt.index('张三',18))#返回值为21。
print(txt.index('张三',6,16))#返回值为8。
