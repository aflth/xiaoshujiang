class Test(object):
    def __init__ (self):
        self.__num = 100

    def setNum(self, number):
        self.__nun= number

    def getNum(self, ):
        return self.__nun

    num = property(getNum, setNum)
    # 在使用property的时候必须先使用getNum在在使用setNum

t = Test()
t.num = 1000
print(t.num)
