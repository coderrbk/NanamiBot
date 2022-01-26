import httpx

async def get_weather(city: str):
    #   这里使用的是聚合数据的api接口 查询天气 （免费）
    #   还请使用这个插件的人自己去申请一个key
    key = "value"
    query = httpx.get("http://apis.juhe.cn/simpleWeather/query?city={}&key={}".format(city,key))
    tianqi = query.json()
    if tianqi["error_code"]!=0:
        return tianqi["reason"]
    else:
        temperature = tianqi['result']['realtime']['temperature']
        humidity = tianqi['result']['realtime']['humidity']
        info = tianqi['result']['realtime']['info']
        direct = tianqi['result']['realtime']['direct']
        power = tianqi['result']['realtime']['power']
        aqi = tianqi['result']['realtime']['aqi']
        return "{}最近的天气状况如下：\n{}，温度：{}℃，湿度：{}%，{}{}，空气质量：{}".format(
            city, info, temperature, humidity, direct, power, aqi)