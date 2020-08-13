import requests, re
from bs4 import BeautifulSoup


url2 = "https://guba.eastmoney.com/list,601216.html"
html2 = requests.get(url2)
page_content2 = BeautifulSoup(html2.text, "html.parser")
rank = page_content2.find("span")
print(rank, type(rank))
print("###########")
print(rank.get_text())