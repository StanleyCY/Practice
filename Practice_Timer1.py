import time as t

class my_timer:

    def __init__(self):
        self.unit = ['年','月','天','小時','分鐘','秒']
        self.begin = 0
        self.end = 0
        self.prompt = '尚未開始計時'
        self.calc = []

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        self.prompt = '提示：記得要執行stop()函數，才能將計時器停止'
        print('計時開始.....')

    def stop(self):
        if not self.begin:
            self.prompt = '提示：記得要先執行start()函數，才能將計時器開啟'
        else:
            self.end = t.localtime()
            print('停止計時.....')
            self._timecheck()#使用self._的方法調用class內的封閉功能

    #_timecheck屬於class內,封閉的功能,所以要使用下底線將function封閉
    def _timecheck(self):
        self.calc = []
        self.prompt = '總共運行了'
        for index in range(6):
            self.calc.append(self.end[index]-self.begin[index])
            if self.calc[index]:   #表示calc is True
                self.prompt += (str(self.calc[index])+self.unit[index])

        #將取得的值self.calc[index]加入儲存變數後，將所有的值恢復成預設值
        self.end = 0
        self.begin = 0

    def __add__(self, other):
        result = []
        self.prompt='兩次總共運行了'
        for index in range(6):
            result.append(self.calc[index]+other.calc[index])
            if result[index]:#表示result is True
                self.prompt += (str(result[index])+self.unit[index])
        return self.prompt
