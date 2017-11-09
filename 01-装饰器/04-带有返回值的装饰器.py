def func(fun):
    print("---func start---")

    def inner(*args, **kwargs):
        print("---inner---")
        return fun(*args, **kwargs)

    return inner


@func
def test1(a, b):
    print("---test1---")
    return a+b


sum = test1(1, 2)
print("a+b=%d" % sum)

