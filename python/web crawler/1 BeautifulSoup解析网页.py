import requests  # 导入requests库，需要安装
from bs4 import BeautifulSoup

"""BeautifulSoupDoc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/ """
# html 文件
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# url = "https://www.jqhtml.com/13272.html"
# res = requests.get(url)
# print(res.status_code)

soup = BeautifulSoup(html_doc, 'lxml')  # 选lxml更有效
# print(soup.prettify())  #用prettify()函数自动补全
# 获取标签、名称、属性、属性、内容
print(soup.title, soup.title.name,
      soup.a['class'], soup.p.attrs['class'],
      soup.title.string,
      sep='\n', end='\n')

common_use = """其他常见用法
find_all(name, attrs, recursive, text, **kwargs)搜索当前tag子节点，并判断是否符合过滤器的条件，列表形式返回
find( name , attrs , recursive , string , **kwargs ) find()返回单个元素
select() CSS选择器标签 class类名加”.“，id属性加”#“，传入字符串参数,
"""

print('0', soup.find_all("title"),  # 找到标签中含有title
      '1', soup.find_all("p", "story"),  # p标签中属性为story
      '2', soup.find_all("a"),  # 找到所有含a的标签
      '3', soup.find_all(id="link2"),  # 获取到link2的a标签
      '4', soup.find_all('p', class_='title'),
      '5', soup.find_all('a', id='link2'),  # 获取到id为link2的a标签
      '6', soup.find_all("a", limit=2),  # 满足的有3个，我们只想要得到2个
      sep='\n', end='\n')

print('0', soup.find('title'),
      '1', soup.find('a'),  # 返回一个结果
      sep='\n', end='\n')

print('0', soup.select('title'),
      '1', soup.select('body a'),  # 通过tag逐层查找
      '2', soup.select("p>a"),  # 找到某个 tag标签下的直接子标签
      '3', soup.select(".sister"),  # 通过CCC的class类名查找
      '4', soup.select("a#link2"),  # 通过 tag 的 id 查找:
      sep='\n', end='\n')

"""提取标签内容"""
lists = soup.find_all("a", class_='sister')  # 找到所有含有sister的a标签
i = 0
for list in lists:
    print(i)
    print(list)  # 打印标签
    # print(list.get_text())  # 使用get_text()方法获得标签内容，文本信息

    print(list['href'], list['id'], list['class'],sep='\n',end='\n')  # 获得标签href的内容

    i = i + 1
