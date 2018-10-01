

dict1 = {"a":"123","b":"234","c":"345","d":"456"}
dict2 = {1:'123',2:'234',3:'345',4:'456'}
print (dict1)
print (dict1['a'])
print ('檢查b索引值是否在dict1字典裡：',dict1.get('b'))
print ('檢查b索引值是否在dict1字典裡：',dict2.get('b'))

print(dict2[1])

dict3 ={}#快速創造空字典的方法
dict3 = dict3.fromkeys(range(1,10),'a')#給予預設的值為"a"
print (dict3)

for eachkey in dict3.keys():
    print (eachkey)
for eachvalue in dict3.values():
    print (eachvalue)
for eachitem in dict3.items():
    print (eachitem)
#dict3.clear()將dicts一次性清除的函數

dict4 = dict3.copy()
print('dict4：',dict4)
print('dict3：',dict3)

dict5 = dict3.pop(6)
print('dict5：',dict5)
print('dict3：',dict3)

dict6 = dict3.popitem()
print('dict6：',dict6)
print('dict3：',dict3)

dict7 = dict3.setdefault(10)
print('dict7：',dict7)
print('dict3：',dict3)

dict8 = dict3.update({10:'b'})
print('dict8：',dict8)
print('dict3：',dict3)



