class Money(object):
    def __init__(self):
        # __前缀的属性只能当前类访问
        self.__money = 0
        # _前缀的属性只能当前类以及他的子类能访问
        self._age = 10

    def getMoney(self):
        return self.__money;

    def setMoney(self, money):
        if isinstance(money, int):
            self.__money = money
        else:
            print("error:传入的不是数字")
    # 改方法必须get方法写前面，set方法写后面
    money = property(getMoney, setMoney)


# 接下来对私有属性额访问直接访问即可，不需要调用get/set方法
test1 = Money()
test1.money = 30
money = test1.money
print("test1money=%d" % money)


# 或者也可以向下面的写法
class Money1(object):
    def __init__(self):
        # __前缀的属性只能当前类访问
        self.__money = 0

    @property
    def money(self):
        return self.__money;

    @money.setter
    def money(self, money):
        if isinstance(money, int):
            self.__money = money
        else:
            print("error:传入的不是数字")


test2 = Money1()
test2.money = "sdsdf"
print("test2money=%d" % test2.money)
print("test2money=%d" % test2.money)
print("test2money=%d" % test2.money.__sizeof__())
