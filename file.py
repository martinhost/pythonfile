# 要求：1、将小甲鱼对话单独保存为boy_*.txt，小客服对话单独保存为girl_*.txt 2、文中有三段话，分别保存为boy_1,2,3,girl_1,2,3共6个文件。文件中不同已经用“======”隔开
#思路分析：先用split方法将boy和girl内容分别放到一个列表文件中，然后再进行保存。具体来说：先打开文件，然后用for循环读取每行并判断是否是"=====",r若不是则将boy和girl对话分别保存。若是则说明，这段文件已经读完，那么创建文件名进行保存

'''
count = 1
boy = []
girl = []
f = open("/pythonfile/test.txt")
for each_line in f:
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':', 1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if girl == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy = []
        girl = []
        count += 1

boy_file = open((pythonfile/ %s' % file_name_boy), 'w')
girl_file = open((pythonfile/ %s' % file_name_girl), 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()
    f.close()
'''

# 封装后程序：分为存储和分割两大部分
def save_file(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(('/pythonfile/ %s' % file_name_boy), 'w')
    girl_file = open(('/pythonfile/ %s' % file_name_girl), 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    count = 1
    boy = []
    girl = []
    
    f = open(file_name)
    for each_line in f:
        if each_line[:6] != '======':
            (role, spoken_line) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(spoken_line)
            if role == '小客服':
                girl.append(spoken_line)
            else:
                save_file(boy, girl, count)

                boy = []
                girl = []
                count += 1
    save_file(boy, girl, count)
    f.close()

split_file('/pythonfile/test.txt')






