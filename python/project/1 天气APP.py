import requests
from django.shortcuts import render

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