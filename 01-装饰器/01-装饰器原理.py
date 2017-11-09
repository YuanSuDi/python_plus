def test(fun):
    def inner():
        print("--inner--")
        fun()
    return inner


def f1():
    print("my name is f1")


def f2():
    print("my name is f2")


f2 = test(f2)
f2()

# a = (x for x in range(20))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print("-"*20)
# for x in a:
#     print(x)
