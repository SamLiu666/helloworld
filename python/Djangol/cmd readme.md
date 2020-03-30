内置的 urls -> 新建的main.urls -> main. views 视图

cmd 指令创建Django 项目

Ctrl-Break   Ctrl-C

```java
// create project Django
django-admin startproject mysite 

// 在创建文件下运行服务器
python manage.py runserver

// 默认端口8080， 添加5050 可改变端口
python manage.py runserver 5050

python manage.py startapp main   // 创建主文件夹

```

```  python
views.py  # 表示网页的视图，显示内容
urls.py   # 决定要访问的视图路径
python manage.py migrate		#确定已经更改
python manage.py makemigrations main	# 改变数据模型

```

```
# <QuerySet [<ToDoList: Ton's List>, <ToDoList: Tim's List>, <ToDoList: First Lis>, <ToDoList: Second Lis>]>

python shell
from main.models import Item, ToDoList
 t = ToDoList.objects
ToDoList.objects.all()
t.filter(name__startswith="Tim")
t,delete()
t.all()
```

<QuerySet [<ToDoList: Ton's List>, <ToDoList: Tim's List>]>



### 模板制作动态HTML

模板继承

 block 可覆盖的部分

```html
!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sam's Website</title>
</head>
<body>
      <div id="content", name = "content">
          {% block content %}
          {% endblock %}
      </div>
</body>
</html>
```

