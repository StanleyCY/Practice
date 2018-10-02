str1 = 'i love Stanley so much '

print(str1.capitalize())#將字串第一個英文字母變成大寫
print(str1.casefold())#將字串的所有英文全部改成小寫
print(str1.count('e'))#尋找某文字在此字串出現的次數
print(str1.center(40))#將字串居中對齊
print(str1.startswith('i'))#檢查字串的開頭是否是以搜尋值作為結束
print(str1.endswith('h'))#檢查字串的結尾是否是以搜尋值作為結束
print(str1.find('x'))#檢查搜尋值在字串中的位置(由左向右檢查),錯誤時回傳-1
print(str1.rfind('e'))#檢查搜尋值在字串中的位置(由右向左檢查)
print(str1.index('e'))#檢查搜尋值在字串中的位置(由左向右檢查),找不到時系統會報錯
print(str1.isalnum())#方法檢測字符串是否由字母和數字組成
print(str1.join('@@@'))#以指定字符串作为分隔符，将字串中所有的元素(的字符串表示)合并为一个新的字符串
print(str1.partition('e'))#找到搜尋的字串後，將前後的字串改成共三組的tuple型式
print(str1.replace('e','E',3))#把將字符串中的str1 替換成str2,如果最後一個參數指定了，則替換不超過指定的次數
print(str1.split())#以特定的值進行字串切割,如無輸入時以空白值進行字串切割,如後面有帶參數,則切割不超過指定的次數
print(str1.strip())#刪除字串中,前後的空白值
print(str1.swapcase())#將字串大寫改成小寫,小寫改成大寫



