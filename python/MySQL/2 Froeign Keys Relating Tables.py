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
