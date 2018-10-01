from random import randint

print('------Class 縱向繼承練習_-------------------')
class person:
    def __init__(self):
        self.x = randint(0,10)
        self.y = randint(0,10)
    def move(self):
        print ('我現在的位置在',self.x,self.y)
class hand:
    def pick(self):
        print('I can pick up any thing')


class blackman(person):
    pass

class yellowman(person,hand):#多重繼承
    def __init__(self):
        super().__init__()#使用super函數將person父類的init 函數拿來使用
        #person.__init__(self) #或使用此方法亦可將父類function拿出來使用
        self.eat = 25
    def eats(self):
        print('I can eat so much,',self.eat,'pcs')


stanley = person()
stanley.move()

tom = blackman()
tom.move()

jerry = yellowman()
jerry.move()
jerry.eats()
jerry.pick()



