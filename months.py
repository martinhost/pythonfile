# 输入一个数得出是几个月多少天

number = int(input("请输入一个数："))
months = number // 30 # 求商
days = number % 30 # 求余

print("{}天是{}月零{}天".format(number, months, days))

#另外一种更简便的方法
'''
number = int(input("Enter numbers:"))
print("Months = {} Days = {}".format(*divmod(days, 30)))

'''
# divmod(num1, num2)返回一个元祖，其中包含两个值，第一个是num1和num2相整除得到的值，第二个是它俩求余得到的值，然后用*运算符拆封这个元祖
