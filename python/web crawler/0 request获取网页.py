import requests
"""
get(url, params=None, **kwargs)
get: 模拟发起请求;
url: 获取网页的url链接
params: 额外参数 字典或字节流格式，可选
**kwargs: 十二个控制访问参数，比如可以自定义header
返回: 一个Response对象
"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

def create_headers():
    # 1.自定义一个header头文件
    url = 'http://www.baidu.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    res = requests.get(url, headers=headers)
    # print(res.request.headers, 'res.status_code, res.text')
    return res


def define_ip_pool():
    # 2.自定义一个代理池
    pxs = { 'http': 'http://user:pass@10.10.10.1:1234',
            'https': 'https://10.10.10.1:4321' }
    r = requests.get('http://www.baidu.com', proxies=pxs)


def know_response():
    res = create_headers()
    print('0',res.status_code,  # HTTP响应情况，200表示成功，404表示失联
          '1',res.headers,      # HTTP请求中的headers
          '2',res.encoding,     # 响应的内容编码方式
          '3',res.content,      # 响应内容的二进制形式
          # '4',res.text,         # 响应内容文本形式
          sep='\n',end='\n')


def get_url_content(url):
    # url要抓取的网页链接
    try:
        res = requests.get(url, headers=headers)
        # 响应未成功，触发异常
        res.raise_for_status()
        # 正确的编码方式
        res.encoding = res.apparent_encoding
        print(res.encoding)
        return res.text
    except:
        return "Wrong!"

if __name__ == '__main__':
    print(get_url_content("https://zhuanlan.zhihu.com/p/26681429"))