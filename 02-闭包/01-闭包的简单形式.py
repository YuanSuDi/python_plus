def test(num):
    print("--test--")

    def test1(num1):
        print("--test1--")
        n = num+num1
        print("num+num1=%d" % n)
    print("--no-test--")
    return test1


# 会调用test方法，但不会调用test1
t = test(23)
# 会调用test1方法，不会调用test方法
t(30)

