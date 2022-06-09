# 逢7的倍数或含7的的数字跳过的小游戏（100以内）
i = 1
while i < 101:

    # 把i转换成字符串，使用find方法（若字符串中不含7则返回-1）
    include = str(i).find('7')

    # 判断条件：既不包含7，也不是7的倍数
    if include == -1 and i % 7 != 0:
        print(i)
        # print(i, end="、") 去掉了了换行符并加了顿号
    i += 1
