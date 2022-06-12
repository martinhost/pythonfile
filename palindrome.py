# 回文检查程序
s = input("Please enter a string:")
z = s[::-1] # 把输入的字符串s进行反转
if z == s:
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome!")
