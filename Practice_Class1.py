class personal():
    __number = 18 #__兩個下底線的動作,將calss內的某個元素封閉起來,因此外界無法調用
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    def walk(self):
        print('I always with',self.name)
    def talk(self):
        print('I always talk with other I\'m',self.grade,'now')
    def care(self):
        print('when I\'m',self.age,',I can take myself')

PersonA = personal('Stanley',6,25)
PersonA.walk()
PersonA.talk()
PersonA.care()
print  (PersonA._personal__number)#想要調用class內封閉條件時,需使用_class__條件才能調用出來)