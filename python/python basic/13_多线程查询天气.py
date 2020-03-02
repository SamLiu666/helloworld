import requests,threading
"""添加改动"""
"""以多线程的方式获取苏州、南京、长沙、娄底、福州的天气
线程中资源问题，可用锁的方式解决"""


def get_weather(city):
    """完整URL：http://open.weather.com.cn/data/?areaid=""&type=""&date=""&appid=""&key=".urlencode($key);"""
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city) # 中国天气接口
    dic_city = req.json() # 转换为字典

    city_data = dic_city.get('data')
    # print(city_data)

    if city_data:
        city_forecast = city_data['forecast'][0]
        print(
            city_data.get('city'),
            city_forecast.get('date'),
            city_forecast.get('high'),
            city_forecast.get('low'),
            city_forecast.get('type'),
            '   '
        )
    else:
        print('未获得')


# cities = ['苏州', '娄底', '福州', '北京', '南京']
cities = [ '娄底', '永泰', '福州', '长沙','苏州','南京']
threads =  []
files = range(len(cities))
for i in files:
    t = threading.Thread(target = get_weather, args=(cities[i],))
    threads.append(t)

for i in files:
    threads[i].start()

for i in files:
    threads[i].join() #多线程进行
print('\n查询结束')

for i in files:
    get_weather(cities[i])


# 进程死循环，CPU占用率极高
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
#     t.join()