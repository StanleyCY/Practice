f = open('C:/practice.txt', 'r')
context = f.readlines()


def writetext(i, boy, girl):
    boy_txtname = 'boy_' + str(i) + '.txt'
    girl_txtname = 'girl_' + str(i) + '.txt'
    with open(('c:/' + boy_txtname), 'w') as f1:
        f1.writelines(boy)
        f1.close()#此代碼也可以省略不寫，因為以with函數調用後,完成會自動關閉文件
        boy.clear()
    with open(('c:/' + girl_txtname), 'w')as f2:
        f2.writelines(girl)
        f1.close()#此代碼也可以省略不寫,完成會自動關閉文件
        girl.clear()


def splittext():
    i = 1
    boy = []
    girl = []
    for eachline in context:
        if eachline[:5] != '=====':
            [role, speak] = eachline.split(':')
            # a = eachline.split(':')
            # print(a)
            if role == '小魚':
                boy.append(speak)
            else:
                girl.append(speak)
        else:
            writetext(i, boy, girl)
            i += 1
    writetext(i, boy, girl)


splittext()
f.close()
