# 求最大公约数

def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d的最大公约数是%d" % (num, count))
            break
        count -= 1
    else:
        print("%d是一个素数！" % num)

try:
    num = int(input("Please enter a number:"))
    showMaxFactor(num)
except ValueError as reason:
    print("输入的数据类型错啦！要输入数字哦~~~" + str(reason))

