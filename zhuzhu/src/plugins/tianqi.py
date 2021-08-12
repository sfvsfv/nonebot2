import urllib.request
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import urllib, requests
from urllib import parse
from nonebot.rule import to_me
weather = on_command("天气",rule=to_me(), priority=5)


# weather=on_keyword({'天气'})
@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询神马城市的天气(@_@)...")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    cityname = city
    # print(cityname)
    url = 'http://apis.juhe.cn/simpleWeather/query?city=%s&key=a8b3dd5052f0e3e2dff14175165500d6' % urllib.parse.quote(
        cityname)
    # print(url)
    data = requests.get(url=url, timeout=5).json()
    # print(data)
    # to=resp['result']['future'][0]
    t = "时间：" + data['result']['future'][0]['date']
    w = "温度:" + data['result']['future'][0]['temperature']
    e = "天气：" + data['result']['future'][0]['weather']
    f = "风向：" + data['result']['future'][0]['direct']

    a = "时间：" + data['result']['future'][1]['date']
    b = "温度:" + data['result']['future'][1]['temperature']
    c = "天气：" + data['result']['future'][1]['weather']
    g = "风向：" + data['result']['future'][1]['direct']
    return str(t + '\n' + w + '\n' + e + '\n' + f + '\n\n\n' + a + '\n' + b + '\n' + c + '\n' + g)
