# def increment(list1):
#     str1 =''
#     for number in list1:
#         str1 += str(number)
#     result = int(str1)+1
#     finish = list(str(result)[-1:-5:-1])
#     finish.reverse()
#     newlist = [int(x) for x in finish]
#     return newlist
#
# print (increment([0,0,9,9]))


# a = [0,8,9,9]
# def s(n):
#     return n+1 if n < 9 else (n+1) % 10
#
# abc = list (map(lambda  x:s(x),a))
#
# print (abc)

def increment(List):
    num = ''.join(str(x) for x in List)
    newnum = int(num)+1
    newlist = list(str(newnum).zfill(len(List)))
    return [int(x) for x in (newlist[-1:-5:-1])]

print (increment([9,0,9,9]))

# def increment(self , add=1 , output=[]):
#     for index , value in enumerate ( self[ ::-1 ] ):
#         add += value * 10 ** (index)
#         output.insert ( 0 , (add // 10 ** index) % 10 )
#     return output
# print (increment([ 0 , 0 , 9 , 8 ]))