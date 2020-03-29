import mysql.connector
from datetime import datetime

# 在 madatabase 的基础上改进
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    auth_plugin="mysql_native_password",  # 必要的密码解码方式
    database = "mydata"
)

mycursor = db.cursor()

sql = """
CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM( "M", "F", "O") NOT NULL,
id int PRIMARY KEY NOT NULL AUTO_INCREMENT)
"""

mycursor.execute(sql) #表添加完成
# 1、插入符合数据格式的数据
mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("Sam", datetime.now(), "M"))
mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("Zoey", datetime.now(), "F"))
mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("Qiang", datetime.now(), "M"))
db.commit()

# 2、选择高级语法
mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")  # 从Test 数据表中选取所有的男性，并以降序输出
mycursor.execute("SELECT name, id FROM Test WHERE gender = 'M' ORDER BY id DESC")  # 只输出选择的名字和ID

# 3、改变行或者列的方式，ALTER
mycursor.execute("ALTER TABLE Test ADD COLUMN Taste VARCHAR(50) NOT NULL")
# 删除一行 DROP
mycursor.execute("ALTER TABLE Test DROP food")
# 改变指定位置的名称,name - Name
mycursor.execute("ALTER TABLE Test CHANGE name Name VARCHAR(50)")

mycursor.execute("DESCRIBE Test")   # 描述表格
print(mycursor.fetchone())      # 选取 一个输出

for i in mycursor:
    print(i)
