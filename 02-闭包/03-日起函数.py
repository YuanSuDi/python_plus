import time

print("--当前日期--")
# print(datetime.date(2017, 11, 12))
# print(datetime.datetime(2017, 11, 12))
# 设置时间格式
ISOTIMEDORMAT = '%Y-%m-%d %X'
print(time.time())
print(time.localtime())
print(time.strftime(ISOTIMEDORMAT, time.localtime()))
print("当前时区与0时区的差值=%s" % time.timezone)
