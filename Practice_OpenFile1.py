import os

f = open('c:/practice.txt','r')
str1 = f.read()
print('str1\n'+str1)
str2 = f.read()#上述的read函數已將檔案讀出,所以讀取器停留在文件的最末端
print('str2\n'+str2)
f.seek(0,0)#將讀取器的位置重新定義至文件的一開始的位置
str3 = f.read()
print('str3\n'+str3)

f.seek(0,0)
print('重新讀取資料')
for eachline in f:
    print (eachline)

f = open('C:/practice.txt','a')
f.write('\ntesttestets')
print(f.tell())
f.close()


