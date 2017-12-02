def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr


c1 = counter(5)
print(c1())
print(c1())

c2 = counter(50)
print(c2())
print(c2())
# 由于C1C2两个地址不同，所以每个变量都对应的自己的属性和数值
print(c1())
print(c1())

print(c2())
print(c2())

start1 = c1()
start2 = c2()
print("c1_id=%s" % id(c1()))
print("c2_id=%s" % id(c2()))
print("---------------------")
print("c1_id=%s" % id(start1))
print("c2_id=%s" % id(start2))

