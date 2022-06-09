temp = input("猜一个数字：")
guess = int(temp)

while guess != 8:
    if guess > 8:
        print("大了！")
    else:
        print("小了！")
    temp = input("再试试？")
    guess = int(temp)

print("你才对了！")
