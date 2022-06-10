# 求N个数的平均数

N = 10
count = 1
sum = 0
print("please input 10 numbers:")

#循环输入10个数字
while count <= 10:
    number = float(input())
    sum += number
    count += 1

average = sum / N #计算平均值
print("N = {}, Sum = {}".format(N, sum))
print("这10个数字的平均值为：{:.2f}".format(average))

