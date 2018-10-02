import time as t

class my_timer:

    def __init__(self):
        self.begin = 0
        self.end = 0
        self.prompt = '尚未開始計時'
        self.calc = []

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.time()
        self.prompt = '提示：記得要執行stop()函數，才能將計時器停止'
        print('計時開始.....')

    def stop(self):
        if not self.begin:
            self.prompt = '提示：記得要先執行start()函數，才能將計時器開啟'
        else:
            self.end = t.time()
            print('停止計時.....')
            self._timecheck()#使用self._的方法調用class內的封閉功能

    #_timecheck屬於class內,封閉的功能,所以要使用下底線將function封閉
    def _timecheck(self):

        self.prompt = '總共運行了'
        self.calc = self.end-self.begin
        if self.calc:   #表示calc is True
            self.prompt += (str(self.calc)+'秒')
    #計算完兩個時間點的時間差後，將所有的值恢復成預設值
        self.end = 0
        self.begin = 0

    def __add__(self, other):
        self.prompt='兩次總共運行了'
        result = self.calc + other.calc
        if result:#表示result is True
            self.prompt += (str(result)+'秒')
        return self.prompt
