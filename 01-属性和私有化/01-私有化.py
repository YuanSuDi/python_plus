class Money(object):
    def __init__(self):
        # __前缀的属性只能当前类访问
        self.__money = 0
        # _前缀的属性只能当前类以及他的子类能访问
        self._age = 10

    def getMoney(self):
        return self.__money;

    def setMoney(self, money):
        self.__money = money


class Test1(Money):
    def __init__(self):
        super().__init__()
        print("age=%d" % self._age)
        # print("money=%d" % self.getMoney())


test1 = Test1()
test1.setMoney(233.333)
money = test1.getMoney()
print("money=%.2f" % money)
