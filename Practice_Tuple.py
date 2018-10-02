print ('-------創建Python tuple的方法-------------')
tuple1 = 1,2,3,4,5 #方法一,不用使用括號
print(type(tuple1))
print (tuple1)

tuple2 = ()#方法二,使用括號創建一個空tuple
print(type(tuple2))
print(tuple2)

tuple3 =(1,)
print (type(tuple3))
print (tuple3)

print ('-------Python tuple加入新元素的方法-------------')
tuple1 = tuple1[:1]+(3,4)+tuple1[1:] #在指定的位置,加入元素到tuple內
print(tuple1)

print ('-------Python tuple刪除新元素的方法-------------')
del tuple1 #tuple內的元素有著不可被修改的特性,所以只能刪除整個tuple,無法單純刪除某一個元素
print(tuple1)


