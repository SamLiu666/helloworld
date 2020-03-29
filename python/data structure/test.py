import mysql.connector

# 链接到SQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",auth_plugin='mysql_native_password'
)
