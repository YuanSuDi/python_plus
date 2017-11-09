def test(fun):
    def inner():
        print("--inner--")
        fun()
    return inner


# 这里的@test就相当于前面的f1 = test(f1),只不过是另一种表现形式
@test
def f1():
    print("my name is f1")


@test
def f2():
    print("my name is f2")


f1()
