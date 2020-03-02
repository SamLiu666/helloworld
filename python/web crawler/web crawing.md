# Definition

Web crawler is used for getting messages from the Internet by following related rules.

The process of web data collection is like a crawler or spider roaming the web. This is why called web crawler or web spider

# Application 

In the ideal situation, all the ICP (Internet Content Provider) should provide their own websites API (Application Programming Interface) interface to share they allow other applications access to data, the crawler, it is not necessary in this case, the domestic famous electric business platform.

# Legitimacy and Background 

Follow the rules, Robots contracts.

Like Baidu: Open the link: https://www.baidu.com/robots.txt . U can see picture 

![image-20200301231430379](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200301231430379.png)

# Tools

HTTP contracts

# Practice

A basic crawler is usually divided into data acquisition (web page download), data processing parsing (web page), and data storage (persistence) will be useful information, the content of the three parts, of course, more advanced crawler they have been used in data acquisition and processing or distributed concurrent programming technology, which requires a scheduler (arrange the thread or process to perform the corresponding task), background management program (monitoring work state of the crawler and the results of the inspection data fetching).

## Steps

1. choose which url
2. try to visit url and get response (header user_client)
3. parser url: BeautifulSoup to fetch information



SSL (Secure Sockets Layer)

1、pycharm

--  Tab 4 right characters 

--   shift+Tab  4 left  characters



# Module

1. download data - urllib / requests / aiohttp。
2. parser data - re / lxml / beautifulsoup4（bs4）/ pyquery。
3. store - pymysql / sqlalchemy / peewee/ redis / pymongo。
4. Generate digital signature - hashlib。
5. Serialization and compression - pickle / json / zlib。
6. scheduler - 进程（multiprocessing） / 线程（threading） / 协程（coroutine）