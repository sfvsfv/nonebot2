from nonebot import on_command
from nonebot.adapters.cqhttp import Event
import requests
from nonebot.adapters.cqhttp import Bot
from nonebot.rule import to_me
weather = on_command("星座运势",rule=to_me(), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询神马星座的运势(@_@)...")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await xin(city)
    await weather.finish(city_weather)


async def xin(city: str):
    cityname = city
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    url = 'http://web.juhe.cn:8080/constellation/getAll?consName=%s&type=today&key=e5a01b4c805febdb3b47f4d8fee618c3' % str(
        cityname)
    d = requests.get(url=url,headers=headers).json()
    data = d['summary']
    return data
