import pymysql


# 查询
def query():
    # 打开数据库链接
    db = pymysql.connect("59.110.172.44", "root", "t2233", "test2")

    # 使用cursor()创建一个游标对象cursor
    cursor = db.cursor()

    # 执行语句
    cursor.execute("select id,name,age,gender from demo WHERE id>0")

    # 获取数据
    datas = cursor.fetchall()

    for row in datas:
        id = row[0]
        name = row[1]
        age = row[2]
        gender = row[3]
        print("id=%d,name=%s,age=%s,gender=%s" % (id, name, age, gender))

    # 关闭数据库链接
    db.close()


# 创建表
def create():
    db = pymysql.connect("59.110.172.44", "root", "t2233", "test2")
    cursor = db.cursor()
    sql = '''
            create table demo2(
            id INTEGER not NULL ,
            username CHAR(32) not NULL )
            '''
    # sql语句换行时，需要使用转义符号
    # sql = 'create table demo2(\
    #             id INTEGER not NULL ,\
    #             username CHAR(32) not NULL )\
    #       '
    cursor.execute(sql)
    db.close()


# query()


# 插入

def insert():
    db = pymysql.connect("59.110.172.44", "root", "t2233", "test2")
    cursor = db.cursor()
    sql = '''
            insert into demo(name,age,gender) 
            VALUES('%s','%d','%s') 
            % ('王五'.decode("utf-8"),23,'女'.decode("utf-8"))
    
            '''
    cursor.execute(sql)
    db.close()


insert()