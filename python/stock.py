# 引入 requests 模組
import requests, re
from bs4 import BeautifulSoup


headers = {
# User-Agent: 在设置用户标识，可以通过该键伪装成是浏览器在访问该网站。而爬虫默认的UserAgent的值是：Python-urllib/2.7。
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
# 使用 GET 方式下載普通網頁
html = requests.get('https://guba.eastmoney.com/remenba.aspx?type=1', headers=headers)
print(html.status_code, type(html))

# 解析页面
page_content = BeautifulSoup(html.text, "html.parser")
page = page_content.find("ul", attrs={"class":"list clearfix"})
stock_name = page.find_all("a")
# print(stock_name, "\n", type(stock_name))

stock_dic = {}
for p in stock_name:
    # print(type(p))
    name = p.get_text()
    link = "https://guba.eastmoney.com/" + p["href"]
    stock_dic[name] = link
    print(name, ": ", link)
# print(stock_dic)

# def crawl_rank(url2):
#     html2 = requests.get(url2)
#     page_content2 = BeautifulSoup(html2.text, "html.parser")
#     rank = page_content2.find("span")
#     print(rank.get_text())
#     return rank
#
# rank_dict = {}
# for s,l in stock_dic.items():
#     v = crawl_rank(l)
#     rank_dict[s] = v
#     print(s,":", v)

