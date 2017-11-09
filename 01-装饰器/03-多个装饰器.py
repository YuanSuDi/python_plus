def makeBold(fun):
    def wrapped(wold):
        print("---makeBold---")
        return "<b>%s</b>" % fun(wold)
    return wrapped


def makeItalic(fun):
    def wrapped(wold):
        print("---makeItalic---")
        return "<i>%s</i>" % fun(wold)
    return wrapped


"""
    这里操作大概分两步
    1. write = makeBold(write)
    2. write = makeItalic(write)
"""


@makeBold
@makeItalic
def write(wold):
    return wold

# write = makeBold(write)
# write = makeItalic(write)


print(write("safsasafas"))
