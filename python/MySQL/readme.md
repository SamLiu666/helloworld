# 安装MySql
数据库学习，python

数据库，可想象成一堆又一堆的数据，类似楼房。 每一栋楼里有不同的数据类型，如公司，公司名称，类型，人员等等，通过各种操作将另一栋的数据联系起来。另一栋楼如公司楼层租金，人员开销等等。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200329222202974.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2ZvbGxvd1VyaGVhcnQ2,size_16,color_FFFFFF,t_70)
## 遇到的问题及解决办法
**mysql 无法连接 Unable to load authentication plugin 'caching_sha2_password'.**
进入mysql 操作空间，按下列代码步骤讲密码的 解码方式从'caching_sha2_password'.* 变为 mysql_native_password 同时更改密码为admin，密码可任意定

```powershell
​```python
mysql -h localhost -u root -p

password

use mysql

select user,host,plugin,authentication_string from user;

# 密码改为admin
alter user 'root' @'localhost' identified with mysql_native_password by 'admin';
```
#  初始 mysql - python
注意：代码中间的添加执行等语句，成功执行之后不要再反复运行。运行成功代表数据库已经添加数据，反复操作会报错。

```python
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
```
# 数据库操作语法
**插入、删除，添加，查询等语法，注意事项同前**

```python
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
```
# 数据库 数据表相互关联
外键的方式，将两个数据表相互关联。仔细查看代码，数据库的语法逻辑计较简单，更高阶的操作可以查看mysql进阶语言学习，注意事项同前
```python
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
users = [
    ("sasha", "yech"),
    ("sasha2", "yech2"),
    ("sasha3", "yech3")
]
user_scores = [
    (45,100),
    (30,200),
    (46,124)
]
mycurcor = db.cursor()

Q1 = "CREATE TABLE Users(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(Id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

## 厨房间列表
# mycurcor.execute(Q1)
# mycurcor.execute(Q2)
# mycurcor.execute("SHOW TABLES")  #显示所有的数据列表
# for i in mycurcor:
#     print(i)

## 插入列表
Q3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userID, game1, game2) VALUES (%s, %s, %s)"

#  一次性插入数据语句
# mycurcor.executemany("INSERT INTO Users (name, passwd) VALUES (%s, &s)", users)

for x, user in enumerate(users):
    mycurcor.execute(Q3, user)
    last_id = mycurcor.lastrowid
    mycurcor.execute(Q4, (last_id,) + user_scores[x])

db.commit()

mycurcor.execute("SELECT * FROM Scores")
for x in mycurcor:
    print(x)

mycurcor.execute("SELECT * FROM Users")
for x in mycurcor:
    print(x)

```
# 总结
数据库是进行计算机学习的必不可少的一部分，了解整个开发流程，做到心中有数，先做到面广再而求精