import mysql.connector

# 链接到SQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    auth_plugin="mysql_native_password",  # 必要的密码解码方式
    db = "mydata"

)

# 提前创建数据库 mydata
# 创建光标，查询
mycursor = db.cursor()
# mycursor.execute("SHOW DATABASES") # 显示数据库是否存在

# 使用 execute() 方法执行 SQL，如果表存在则删除
# mycursor.execute("DROP TABLE IF EXISTS PERSON")
# 使用预处理语句创建表
sql = """CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, 
personID int PRIMARY KEY AUTO_INCREMENT)"""
# mycursor.execute(sql)

for x in mycursor:
    print(x[0])





