def math1(number):
    for count in range(number-1,2,-1):
        if number % count == 0:
            print(number, '不為質數，最大的公約數為', count)
            break
    else:
        print(number,'為質數')

a = input('請輸入您想要檢驗的數字：')
math1(int(a))
