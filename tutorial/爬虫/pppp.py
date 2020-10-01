import pandas as pd
from selenium import webdriver
import time, requests, random
from bs4 import BeautifulSoup


def parse(soup, number):
    lists = soup.find('div', id="hotel_lst_container").find('ul')
    all_lists = []
    if lists:
        print("######\n Start Parsing ")
        for list in lists:
            name = list.find('a', class_="hotel-name").get_text()
            address = list.find('p', class_="adress").get_text()
            comment = list.find('span', class_='infor').get_text()
            amount = list.find('span', class_='total').get_text()
            type = list.find('span', class_='type').get_text()
            lowest_price = list.find('a', href="/cn/foshan/dt-10041/")
            goods = {'序号': number,
                     '酒店名称': name,
                     '地址': address,
                     '评价': comment,
                     '点评数': amount,
                     '类型': type,
                     '价格': lowest_price}
            print(number, name, address, comment, amount, type, lowest_price)
            #print("done")
            all_lists.append(goods)
            number += 1
        return all_lists, number, True
    else:
        print("####\n Not Parsing! ")
        return all_lists, number, False

def write_csv(all_lists, EXCEL_PATH):
    # EXCEL_PATH = '酒店信息1.xlsx'
    df = pd.DataFrame(all_lists)
    writer = pd.ExcelWriter(EXCEL_PATH)
    df.to_excel(excel_writer=writer, columns=['序号', '酒店名称', '地址', '评价', '点评数', '价格'], index=False,
                encoding='utf-8', sheet_name='Sheet')
    writer.save()
    # writer.close()
    print("######### record done")

# 1.build webdriver chrome
driver = webdriver.Chrome()  # 初始化一个浏览器对象
#print(driver)

# 2. get the page
url = "https://hotel.qunar.com/cn/foshan/?fromDate=2020-09-30&toDate=2020-10-01&cityName=%E4%BD%9B%E5%B1%B1"
driver.get(url)
# print(type(driver.page_source))
number,page_num = 1,1

for i in range(4):
    # 3. parse the page
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print("############# Current Page", page_num)
    record, count, flag = parse(soup, number)

    if not flag:
        #  刷新本页
        driver.refresh()
        continue
    # 4. write to file
    EXCEL_PATH = "file_path.xlsx"
    write_csv(record, EXCEL_PATH)

    # 5. next page
    # selenium的xpath用法，找到包含“下一页”的a标签去点击
    next_button_xpath = "/html/body/div[2]/div/section/section[1]/aside[1]/div[6]/p[1]"
    driver.find_element_by_xpath(next_button_xpath).click()
    time.sleep(6)  # 睡2秒让网页加载完再去读它的html代码
    page_num += 1
    number = count