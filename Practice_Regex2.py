import re

def strip(str,subword=None):
    if subword == None:
        StrRegex1 = re.compile ( r'^(\s*)(.*\S)(\s*)$' )
        result1 = re.findall(StrRegex1,str)
        return result1[0][1]
    else:
        StrRegex2 = re.compile(subword)
        result2 = StrRegex2.sub(' ', str)
        return result2


str = '    1fawargfaw1243454    '

a = strip(str)
print(a)

b= strip(str,'f')
print(b)



