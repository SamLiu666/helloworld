"""爬取目标
1、爬取百度贴吧：东南大学吧
url = https://tieba.baidu.com/f?ie=utf-8&kw=%E4%B8%9C%E5%8D%97%E5%A4%A7%E5%AD%A6&fr=search
2、分析网页，找到每一篇帖子的标题、发帖人、日期、楼层、以及跳转链接
3、将结果存入文本
"""
import requests
from bs4 import BeautifulSoup


def get_url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
        res = requests.get(url, headers=headers)
        # 响应未成功，触发异常
        res.raise_for_status()
        # 正确的编码方式
        res.encoding = res.apparent_encoding
        # print(res.encoding)
        print(res.status_code)
        return res.text
    except:
        return "Wrong!"


def parser_content(url):
    #获取帖子，并传入soup，进行格式化,初始化存储列表
    html = get_url(url)
    soup = BeautifulSoup(html, 'lxml')
    comments = []

    # 找到所有的帖子的大类标签，返回列表
    tz_tags = soup.find_all('li', attrs={'class' :" j_thread_list clearfix"})

    # 循环每一个标签，找到需要的没有给信息
    for tz in tz_tags:
        # 用字典存储一个帖子的信息
        tz_comment = {}

        # 使用try 防止查找不到信息而停之运行
        try:
            tz_comment['title'] = tz.find('a', attrs={'class':"j_th_tit "}).text.strip()    # 标题
            tz_comment['Link'] = tz.find('a', attrs={'class': 'j_th_tit '})['href']     # 链接
            tz_comment['name'] = tz.find('span', attrs={'class': 'tb_icon_author '}).text.strip()   #发帖人
            comments.append(tz_comment)

        except:
            print('PROBLEM!')
    print(comments)


def Tofile(dic):
    '''以文件形式存储到本地'''
    with open('Teiba.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t '.format(
                comment['title'], comment['link'], comment['name']))

    print('Crawl Done')


def main(base_url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('All done!')

    #写入数据
    for url in url_list:
        content = parser_content(url)
        Tofile(content)
    print('Already Write')


if __name__ == '__init__':
    base_url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%B8%9C%E5%8D%97%E5%A4%A7%E5%AD%A6&fr=search'
    deep = 0
    main(base_url,deep)