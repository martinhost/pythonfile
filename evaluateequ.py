# 求1/x+1/(x+1)+1/(x+2)....+1/n

sum = 0

for i in range(1, 11):
    sum += 1 / i
    print("{:2d} {:6.4f}".format(i, sum))
