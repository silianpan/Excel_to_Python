# 自定义函数。
def level(number,lv1,lv2,lv3):
    if number>=90:
        return lv1
    elif number>=60:
        return lv2
    elif number>=0:
        return lv3
# 自定义函数的调用。
for score in [95,63,58,69,41,88,96]:
    print(score,level(score,'优','中','差'))