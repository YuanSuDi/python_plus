from money import Money


class Test2(Money):
    def __init__(self):
        super().__init__()
        print("age=%d" % self._age)


if __name__ == "__main__":
    test2 = Test2()
    # 单个下横杠的子类均可以访问
    test2._age = 30
    test2.age = 50  # 可以动态添加属性
    print("age=%d,%d" % (test2._age,test2.age))
    test2.setMoney(233.333)
    money = test2.getMoney()
    print("money=%.2f" % money)
