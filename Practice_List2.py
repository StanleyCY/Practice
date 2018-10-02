list1 = ['陳三','李四','王五','黃六','陳一','陳二','李三,王五']
list2 = [1,3,8,2,5,9,1,0,25,23,2,2,2]
print('------Python加入一個新的元素方法---------')
print (list1 + ['123']) #Python加入一個新的元素方法一,要使用[]將元素加進去
list1.append('測試一')   #Python加入一個新的元素方法二,使用append指令將元素加進去
print (list1)
list1.extend(['測試二','測試三']) #Python加入一個新的元素方法三,使用extend指令將另一個列表加進去
list1.insert(0,'測試零')#Python加入一個新的元素方法四,使用insert指令在指定的位置將元素加進去

print('----目前list1的內容-----')
print(list1) #目前list1的內容

print('---------Python列表運用-------')
print(list1 + list2) #列表相加
# print(list1-list2) #不同列表性質,無法相減/相乘/相除
print (2*list1) #複製列表
print (len(list1)) #取得目前列表的長度
print(list1[:])#取得list1所有的內容
print(list1[3])#取得list1中第四個元素
print(list1[:4])#取得list1中第一到四個元素
print(list1[2:])#取得list1中第三到最後一個元素
print(list1[2:5])#取得list1中第3到5的元素
print(list1[::2])#取得list1中所有的元素，每次間隔2

print('---------Python刪除列表元件的方法-------')
list1.remove('測試一')#Python刪除一個新的元素方法一,使用remove指令將元素刪除
print (list1)

del list1[8]#Python刪除一個新的元素方法二,使用del指令將元素刪除
print (list1)

list1.pop(7)
print(list1)#Python刪除一個新的元素方法三,使用pop指令將指定元素刪除,如無指定,預設會刪除最後一個元素


print('---------Python列表整理的指令-------')
print(list2.count(2))#計算list2當中,2出現的次數
print(list2.index(2))#計算list2當中,2第一次出現的位置
print(list2.index(2,3,10))#計算list2當中,指定特定的位置(3-10)之間，2第一次出現的位置
list2.reverse()#將list2元素,從後往前,重新排列list2列表
print(list2)
list2.sort()#將list2元素,從小到大,重新排列list2列表
print(list2)
list2.sort(reverse=True)#將list2元素,從大到小,重新排列list2列表
print(list2)

print('---------Python列表特別要注意的地方-------')
list3 = list2[:] #複製列表時,記得要先將列表切片後再進行複製,否則會產生連動效果,而不是得到一個全新的列表
print (list3)

list3.append([2,5]) #將元件加入列表時,切記要使用append或extend的方法加入元件,切勿使用"+"的方式將元件加入
print(list3)
print(list3[13][1])

# list3.sort() #由於inst和list或者str性質的元件存在於list3列表內，因此無法使用sort功能
# print(list3)
