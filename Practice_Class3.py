print('------Class 橫向繼承練習_-------------------')


class Man:
    def __init__(self, x):
        self.num = x


class Woman:
    def __init__(self, y):
        self.num = y


class Party:
    def __init__(self, x, y):
        self.mantotal = Man(x)
        self.womantotal = Woman(y)

    def printtotal(self):
        print('There\'re %a man and %d woman here !!' % (self.mantotal.num, self.womantotal.num))


partyA = Party(12, 15)
partyA.printtotal()

print('------Class BIF 練習_isinstance-------------------')
print(isinstance(partyA, Man))
print(isinstance(partyA, Woman))
print(isinstance(partyA, Party))

print('------Class BIF 練習_hasattr-------------------')
print(hasattr(partyA, 'mantotal'))
print(hasattr(partyA, 'womantotal'))
print(hasattr(partyA, 'printtotal'))
print(hasattr(partyA, 'x'))
print(hasattr(partyA, 'y'))

print('------Class BIF 練習_getattr-------------------')
print(getattr(partyA,'mantotal'))
print(getattr(partyA,'womantotal'))
print(getattr(partyA,'printtotal'))
print(getattr(partyA, 'x','你所訪問的屬性不存在'))
print(getattr(partyA, 'y','你所訪問的屬性不存在'))

print('------Class BIF 練習_setattr-------------------')
setattr(partyA, 'y','你所訪問的屬性已存在')
print(getattr(partyA, 'y','你所訪問的屬性不存在'))

print('------Class BIF 練習_delattr-------------------')
delattr(partyA, 'y')
print(getattr(partyA, 'y','你所訪問的屬性不存在'))

print('------Class BIF 練習_property-------------------')
class cellphone:
    def __init__(self,money=10000):
        self.money = money
    def getmoney(self):
        return self.money
    def sellmoney(self,lastmoney=20000):
        self.money = lastmoney
    def nomoney(self):
        del self.money
    x = property(getmoney,sellmoney,nomoney)


Sony = cellphone()
print (Sony.getmoney())
Sony.sellmoney()
print (Sony.getmoney())
Sony.nomoney()
print (getattr(Sony,'self.money','你所訪問的屬性不存在'))

Sony.x = 30000 #由於有property函數,可一次性地將值授予class cellphone內的所有功能
print (Sony.getmoney())
Sony.sellmoney(40000)
print (Sony.getmoney())
