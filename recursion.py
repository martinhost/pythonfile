'''
# 阶乘的迭代法
def recursion(n):
    result = 1
    for i in range(1, 6):
        result *= i
    return result

number = int(input("Please enter a number:"))
result = recursion(number)
print("%d的阶乘是：%d" % (number, result))
'''

# 阶乘的递归法

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Please enter a number:"))
result = factorial(number)

print("{}的阶乘是{}".format(number, result))
