while True:
    num = input("请输入一数字(按q退出)：")
    if num == 'q':
        print('GameOver')
        break
    else:
        guess = int(num)
        if guess < 8:
            print("小了点！")
            continue
        elif guess > 8:
            print("大了点！")
            continue
        else:
            print("bingo,你太棒了！")
            break

            

