# 参考

https://getbootstrap.com/docs/4.4/getting-started/introduction/  bootstrap

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

python manage.py startapp name_app   // 创建主文件夹，存放应用代码的地方

 
```

```  python
views.py  # 表示网页的视图，显示内容
urls.py   # 决定要访问的视图路径
python manage.py migrate		#确定已经更改
python manage.py makemigrations main	# 改变数据模型

```

```
# <QuerySet [<ToDoList: Ton's List>, <ToDoList: Tim's List>, <ToDoList: First Lis>, <ToDoList: Second Lis>]>

python manage.py shell
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

# 个人博客

##  创建django 项目

```
// create project Django
django-admin startproject mysite 

// 在创建文件下运行服务器
python manage.py runserver

// 默认端口8080， 添加5050 可改变端口
python manage.py runserver 5050

python manage.py startapp name_app   // 创建主文件夹，存放应用代码的地方
```

setting 更改

1. django 如何接收 HTTP 请求？
2. django 如何处理这个 HTTP 请求？
3. django 如何生成 HTTP 响应？



#  进度

4/7  https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/64/