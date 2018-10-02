str1 = '{0} love {1} so {2} '.format('I','Stanley','much')
print ('str1',str1)

str2 = '{a} love {b} so {c} '.format(a='I',b='Stanley',c='much')
print('str2',str2)

str3 = '{0}'.format('Error')
print ('str3',str3)

str4 = '{{0}}'.format('error')
print ('str4',str4)#特別注意與str3的不同處

str5 = '%c %c %c' % (97,98,99)
print('str5',str5)

str6 = '%s' % 'I love Stanley so much !'
print ('str6',str6)

str7 = '{:x<4d}'.format(5)#大小於的開口方向代表補齊特定符號的方向
print ('str7',str7)

str8 = '{:0>3d}'.format(5)#大小於的開口方向代表補齊特定符號的方向
print(str8)
str8 = '%03d'% 5#%後面加一個0,代表數字前面補齊0共三位寬度的數字
print(str8)


str9 = '{:+.3f}'.format(3.1415926)#f代表四捨五入符號
print ('str9',str9)

str10 = '{:+.0f}'.format(-3.1415926)
print ('str10',str10)

str11 = '{:,}'.format(1234000000000)
print ('str11',str11)

str12 = '{:5.5f}'.format(12.2334364834)
print ('str12',str12)

str13 = '{:g}'.format(12.2334764834)#g代表系統會自動判斷最適合的七個寬度的數字(也會自行四捨五入)
print ('str13',str13)

str14 = '%g' % 12.2334764834#g代表系統會自動判斷最適合的七個寬度的數字(也會自行四捨五入)
print ('str14',str14)

