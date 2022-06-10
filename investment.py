# 计算投资收益的程序

acount = int(input("请输入本金："))
rate = float(input("请输入预期收益率："))
n = int(input("请输入年限："))
year = 1
value = 0 # 收益金额初始化

while year <= n:

    value = acount * (1 + rate)
    print("第 {}年的收益为：{:.2f}".format(year,value))
    acount = value # 将本年收益进行累计
    year += 1
