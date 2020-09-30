from selenium import webdriver
import time, requests, random
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import codecs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def parse(soup, all_lists, number):
    lists = soup.find('div', id="hotel_lst_container").find('ul')
    if lists:
        print("Start Parsing ")
        for list in lists:
            name = list.find('a', class_="hotel-name").get_text()
            address = list.find('p', class_="adress").get_text()
            comment = list.find('span', class_='infor').get_text()
            grade = list.find('span', class_='num').get_text()
            amount = list.find('span', class_='total').get_text()
            lowestprice = list.find('span', class_='type').get_text()
            goods = {'序号': number,
                     '酒店名称': name,
                     '地址': address,
                     '评价': comment,
                     '点评数': amount,
                     '价格': lowestprice}
            number += 1
            print(number, name, address, comment, amount, lowestprice)
            #print("done")
            all_lists.append(goods)
            EXCEL_PATH = '酒店信息1.xlsx'
            df = pd.DataFrame(all_lists)
            writer = pd.ExcelWriter(EXCEL_PATH)
            df.to_excel(excel_writer=writer, columns=['序号', '酒店名称', '地址', '评价', '点评数', '价格'], index=False,
                        encoding='utf-8', sheet_name='Sheet')
            writer.save()
            # writer.close()
        return True
    else:
        print("No message Find")
        return False

def write_csv(all_lists):
    EXCEL_PATH = '酒店信息1.xlsx'
    df = pd.DataFrame(all_lists)
    writer = pd.ExcelWriter(EXCEL_PATH)
    df.to_excel(excel_writer=writer, columns=['序号', '酒店名称', '地址', '评价', '点评数', '价格'], index=False,
                encoding='utf-8', sheet_name='Sheet')
    writer.save()
    writer.close()

driver = webdriver.Chrome()  # 初始化一个浏览器对象
url = "https://hotel.qunar.com/cn/foshan/?fromDate=2020-09-30&toDate=2020-10-01&cityName=%E4%BD%9B%E5%B1%B1"
driver.get(url)
number = 1
page_num = 1

all_lists = []
### for
for i in range(100):
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')  # 从网页提取数据
    print("Page Number: ", page_num)
    if html:
        # 解析网页
        flag = parse(soup, all_lists, number)
        # 点击下一页
        if flag:
            next_str = "//p[@class='next fl_right cur able']"
            btns = driver.find_elements_by_xpath(next_str)
            for a in btns:
                if a.text == u"下一页":
                    a.click()
                    page_num += 1
                    break
        else:
            print("Page Referesh")
            driver.refresh()


