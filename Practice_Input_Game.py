import random

print('-------------以下遊戲開始-------------')
guess = ''
answer = random.randint(1, 10)
i = 1
while guess != answer:
    temp = input('請輸入心中猜想的數字：')
    if i >= 5:
        print('猜太多次數，遊戲關閉！')
        exit()
    try:
        guess = int(temp)
    except:
        i += 1
        print('輸入的值非數字性質，請重新輸入，謝謝！')
        continue
    i += 1
    if answer < guess:
        print('猜錯囉~~ 猜的數字要再小一點，請再嘗試看看!')
    elif answer > guess:
        print('猜錯囉~~ 猜的數字要再大一點，請再嘗試看看!')
    else:
        print('恭喜你!!  你是高手')
print('希望下次再次光臨')
