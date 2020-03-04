import requests
import bs4, csv
import xlwt


"""pycharm:  改了UTF-8还是无法显示汉字 https://www.cnblogs.com/duoxuan/p/12090725.html
"""
movie = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 建立工作区
sheet = movie.add_sheet('电影排行榜', cell_overwrite_ok=True)  # 表名
# 第一行第n列名称
n = 1
sheet.write(0, 0, 'Title')
sheet.write(0, 1, 'Time')
sheet.write(0, 2, 'Actors')
sheet.write(0, 3, 'synopsis')


def get_url(url):
    # 获取网页

    try:
        proxy_list = [
            '183.95.80.102:8080',
            '123.160.31.71:8080',
            '115.231.128.79:8080',
            '166.111.77.32:80',
            '43.240.138.31:8080',
            '218.201.98.196:3128']
        headers = {
            'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "}
        res = requests.get(url, headers=headers, proxy_list = proxy_list)
        res.raise_for_status
        print(res.encoding, res.status_code)
        res.encoding = 'gbk'
        return res.text
    except:
        return 'Wrong!'


def get_content(url):
    html = get_url(url)
    soup = bs4.BeautifulSoup(html, 'lxml')

    #找到电影中存放榜单的标签
    movies_list = soup.find('ul', class_='picList clearfix')
    if isinstance(movies_list, bs4.element.Tag):
        pass
    else:movies = movies_list.find_all('li')

    movie_info = []
    #
    for movie in movies:
        try:
            # 从主树开始向下寻找，字典方式，列表方式
            # movie_dic['name'] = movie.find('span',class_='sTit').a.text
            name = movie.find('a', attrs= {'target':'_blank'}).a.text
            # 上映时间
            # movie_dic['time'] = movie.find('span',class_='sIntro').text
            time= movie.find('span', class_='sIntro').text
            # 电影演员
            actors = movie.find('p', class_ = 'pActor')
            actor = ''
            for i in actors:
                actor = actor + i.string + " "
            # movie_dic['actors'] = actor
            # 电影简介
            # movie_dic['intro'] = movie.find('p', class_ = 'pTxt pIntroShow').text
            intro = movie.find('p', class_='pTxt pIntroShow').text
            print(name,time,actor,intro)
            sheet.write(n, 0, name)
            sheet.write(n, 1, time)
            sheet.write(n, 2, actor)
            sheet.write(n, 3, intro)
            n = n + 1
            # movie_info.append(name, time, actor, intro)
            # sheet.write(n, 0, dict['name'])
            # sheet.write(n, 1, dict['time'])
            # sheet.write(n, 2, dict['actors'])
            # sheet.write(n, 3, dict['intro'])
        except:
            pass

# def writeTofile(dict):
#     """
#     将数据写入文件
#     :param dict: 字典类型数据
#     :return:
#     """
#     # with open('Movie.txt', 'a+') as f:
#     #     for movie in dict:
#     #         f.write('标题： {} \t 上映时间：{} \t 演员：{} \t 简介: \t'.format
#     #             (movie['name'], movie['time'], movie['actors'], movie['intro']))
#
#     # for movie in dict:
#     #     print(movie['name'], movie['time'], movie['actors'], movie['intro'])
#     # 写入CSV 文件
#     movie = xlwt.Workbook(encoding='utf-8',style_compression=0)     #建立工作区
#     sheet = movie.add_sheet('电影排行榜', cell_overwrite_ok=True)    #表名
#     #第一行第n列名称
#     n =1
#     sheet.write( 0, 0, 'Title')
#     sheet.write( 0, 1, 'Time')
#     sheet.write( 0, 2, 'Actors')
#     sheet.write( 0, 3, 'synopsis')
#     while n<= 50:
#         i=0
#         # sheet.write(n, 0, dict[0]['name'])
#         # sheet.write(n, 1, dict[0]['time'])
#         # sheet.write(n, 2, dict[0]['actors'])
#         # sheet.write(n, 3, dict[0]['intro'])
#         n = n + 1
#
#     movie.save('Movie List.xls')

if __name__ == '__main__':
    base_url = "http://dianying.2345.com/top/"
    get_content(base_url)

movie.save(u'Movie List .xls')