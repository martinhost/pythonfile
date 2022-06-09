while True:
    temp = input("请输入一个数字(按q退出)：")
    if temp == 'q':
        print("Game Over")
        break
    else:
        guess = int(temp)
        if guess == 8:
            print("哇哦，你厉害，是我肚里蛔虫！")
            break
        else:
            if guess < 8:
                print("哥，小了点哦！")
                continue
            else:
                print("兄弟，大了点哦！")
                continue

