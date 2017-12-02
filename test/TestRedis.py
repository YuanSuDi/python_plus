import redis

r = redis.StrictRedis(host="59.110.172.44", port="6000", password="wastone@#@#@%$sdsadasdDFGDFGSFDSD*$##$%F@")
# 这里由于得到的是二进制的字符串，需要进行解码操作
# v = r.get('name').decode("utf-8")
# # r.set("name", "zhanssss你好")
# print(v)


r.hmset("dict", {'name': 'zhangsan', 'gender': 'man'})
r.expire('dict', 100)
