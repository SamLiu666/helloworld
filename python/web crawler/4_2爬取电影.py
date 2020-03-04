import requests
import bs4
import xlwt


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        # 该网站采用gbk编码！
        r.encoding = 'gbk'
        return r.text
    except:
        return "someting wrong"


def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')

    # 找到电影排行榜的ul列表
    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')

    for movie in movies:
        # 找到图片连接，
        img_url = movie.find('img')['src']

        name = movie.find('span', class_='sTit').a.text
        # 这里做一个异常捕获，防止没有上映时间的出现
        try:
            time = movie.find('span', class_='sIntro').text
        except:
            time = "暂无上映时间"

        # 这里用bs4库迭代找出“pACtor”的所有子孙节点，即每一位演员解决了名字分割的问题
        actors = movie.find('p', class_='pActor')
        actor = ''
        for act in actors.contents:
            actor = actor + act.string + '  '
        # 找到影片简介
        intro = movie.find('p', class_='pTxt pIntroShow').text
        # 找到电影链接
        link = movie.find('a', class_="aPlayBtn")['href']
        global n
        sheet.write(n, 0, name)
        sheet.write(n, 1, time)
        sheet.write(n, 2, actor)
        sheet.write(n, 3, link)
        sheet.write(n, 4, intro)
        n = n + 1

        print("片名：{}\t{}\n{}\n{} \n \n ".format(name, time, actor, intro))

        # 我们来吧图片下载下来：
        # with open('/Users/ehco/Desktop/img/' + name + '.png', 'wb+') as f:
        #     f.write(requests.get(img_url).content)


def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)


movie = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 建立工作区
sheet = movie.add_sheet('电影排行榜', cell_overwrite_ok=True)  # 表名
# 第一行第n列名称
n = 1
sheet.write(0, 0, '电影')
sheet.write(0, 1, '上映时间')
sheet.write(0, 2, '演员')
sheet.write(0, 3, '连接')
sheet.write(0, 4, '简介')

if __name__ == "__main__":
    "列表形式保存"
    main()

movie.save('movie.xls')