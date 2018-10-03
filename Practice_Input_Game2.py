from random import randint

answer = randint(0,101)

while True:
    guess = int(input('請輸入您想要猜測的數字大小：'))
    if guess > answer:
        print ('猜的數字太大，請重新輸入')
    elif guess < answer:
        print ('猜的數字太小，請重新輸入')
    else:
        print('Bingo !! 恭喜你答對了~ ')
        break