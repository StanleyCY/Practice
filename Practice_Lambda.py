def add (x,y):
    return x+y
print (add(3,4))

result = lambda x,y:x+y
print (result(3,4))

def odd(x):
    return x%2
temp = range(10)
show = filter(odd,temp)
print(list(show))

show = filter(lambda x:x%2,range(10))
print(list(show))

def square(x):
    return x**2
value = map(square,range(10))
print (list(value))

value = map(lambda x:x**2,range(10))
print (list(value))

value = map(lambda x,y:x+y,[1,3,5,7,9],[2,4,6,8,10])
print (list(value))

def math1(n):
    result = n
    for i in range(1,n):
        result = result *i
    return result
print(math1(5))

def math2(n):  #傳說中的遞歸寫法,困難度很高
    if n ==1:
        return 1
    else:
        return n * math2(n-1)
print(math2(5))

def adds(n):#斐波那契數列(運算速度較快)
    n1 = 1
    n2 = 1
    n3 = 1
    if n<1:
        print('輸入錯誤')
    else:
        while n-2>0:
         n3 = n2 + n1
         n1 = n2
         n2 = n3
         n = n-1
        return n3
print(adds(40))

def adds(n):  #斐波那契數列(運算速度較慢)
    if n ==1:
        return 1
    elif n ==2:
        return 1
    else:
        return adds(n-2) + adds(n-1)
print(adds(40))


