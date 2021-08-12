from nonebot import on_command, on_keyword
from nonebot.adapters.cqhttp import Bot, Event
import requests
from nonebot.adapters.cqhttp import Bot
from nonebot.rule import to_me
weather = on_command("成语查询",rule=to_me(), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询神马成语(@_@)...")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await xin(city)
    await weather.finish(city_weather)


async def xin(city: str):
    cityname = city
    url = 'http://apis.juhe.cn/idioms/query?key=3da85cf3b46175276926ceea5238ee0c&wd=' + cityname
    d = requests.get(url=url).json()
    print(d)
    jie = d['result']['xxsy'][0]
    chu = d['result']['xxsy'][1]
    shi = d['result']['xxsy'][2]
    # yu=d['result']['xxsy'][3]
    # j='近义词：'+d['result']['jyc']
    # fyc='反义词：'+d['result']['fyc']
    return str(jie + '\n' + chu + '\n' + shi)
