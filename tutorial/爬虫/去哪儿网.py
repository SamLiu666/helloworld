# coding: utf-8
# @File:poi_train_data crawl_city.py 
# @Time :2020/9/30-10:14
# @Author:WangYan

import requests
from bs4 import BeautifulSoup
import re
import pymysql
import pandas as pd


url = "https://hotel.qunar.com/cn/foshan/?fromDate=2020-09-30&toDate=2020-10-01&cityName=%E4%BD%9B%E5%B1%B1"
headers = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
html = requests.get(url, headers=headers)
print(html)
page = html.text
soup = BeautifulSoup(page, 'html.parser')  # 从网页提取数据
print(soup)
number = 1
print("############################")
if soup:

    lists = soup.find('div', id="hotel_lst_container").find('ul')
    print("lists: ", lists)
    print("#######################")
    all_lists = []

    if lists:

        for list in lists:
            name = list.find('a', class_="hotel-name").get_text()
            address = list.find('p', class_="adress").get_text()
            comment = list.find('span', class_='infor').get_text()
            grade = list.find('span', class_='num').get_text()
            amount = list.find('span', class_='total').get_text()
            lowestprice = list.find('span', class_='y rmb').get_text()
            goods = {'序号': number,
                     '酒店名称': name,
                     '地址': address,
                     '评价': comment,
                     '点评数': amount,
                     '价格': lowestprice}
            number += 1
            print(number, name, address, comment, amount, lowestprice)
            all_lists.append(goods)
            # print(goods)

        EXCEL_PATH = '酒店信息.xlsx'
        df = pd.DataFrame(all_lists)
        writer = pd.ExcelWriter(EXCEL_PATH)
        df.to_excel(excel_writer=writer, columns=['序号', '酒店名称', '地址', '评价', '点评数', '价格'], index=False,
                    encoding='utf-8', sheet_name='Sheet')
        writer.save()
        writer.close()
    else:
        print("List: None")
else:
    print("Can Not Get")

