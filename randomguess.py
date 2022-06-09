import random

secret = random.randint(1, 10)
temp = input("不妨菜一下我现在心里想的是哪个数字：")
guess = int(temp)
times = 1
while (guess != secret) and (times < 3):
    if guess > secret:
        print("大哥，大了大了~~")
    else:
        print("嘿，小了小了~~")
    
    temp = input("请再试试吧：")
    guess = int(temp)
    times = times + 1
if (times <= 3) and (guess == secret):
    print("哎呀，你是我肚里的蛔虫呀！")
    print("哼，猜中了也没有奖励哦~~")
else:
    print("嗯，给三次机会都猜不着，不跟你玩了！")
