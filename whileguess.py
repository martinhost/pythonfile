while True:
    temp = input("请输入你猜的数字(退出请按q)：")
    if temp == 'q':
        print('Game Over')
        break
    else:
        guess = int(temp)
        if guess != 8:
            print("你猜错了！再来！")
            continue
        else:
            print("猜对了！")
            break
