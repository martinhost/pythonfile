#录入学生成绩并判断总成绩是否达标

n = int(input("please enter the number of students:"))
data = {} #用来存储数据的字典变量
Subjects = ('Physicis', 'Maths', 'History') #所有科目
for i in range(0, n):
    name = input("Enter the name of the student {}:".format(i + 1)) # 获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input("Enter marks of {}:".format(x)))) # 获得每一科的分数
    data[name] = marks # 将学科成绩和学生挂钩
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")
