import mysql.connector

# 链接到SQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    auth_plugin="mysql_native_password",  # 必要的密码解码方式
    database = "mydata"
)

# 0 、创建执行光标
mycursor = db.cursor()

# 1、创建 人物表，类似表头
sql = """CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"""
mycursor.execute(sql)     # 执行语句sql，之后对表操作要关闭

mycursor.execute("DESCRIBE Person")         # 描述人物 含有那些信息

 #2、插入数据
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('TOM', 22))
db.commit()     # 确认改变
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('Jacker', 25))
db.commit()     # 确认改变


# 3 查询全部人物
mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    # 打印光标内容
    print(x)