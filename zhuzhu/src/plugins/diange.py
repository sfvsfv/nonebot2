from nonebot import on_command, on_keyword
from nonebot.adapters.cqhttp import Bot, Event, Message
import requests, re
from nonebot.rule import to_me
weather = on_command("酷狗音乐",rule=to_me(), priority=6)
@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想听什么歌呢？小可爱")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.send(message=Message(city_weather))


async def get_weather(city: str):
    cityname = city
    url = 'http://www.crys.top/api/kwdg.php?msg=%s&n=1&c=text'%cityname
    d = requests.get(url=url, timeout=5).text
    tu=re.findall('图片：(.*)',d)[0]
    # print(tu)
    ge=cityname
    # print(ge)
    ur=re.findall('链接：(.*)',d)[0]
    # print(ur)
    yinyue = f"[CQ:music,type=custom,audio={ur},title={cityname},image={ge},image={tu}]"
    return yinyue

weather = on_command("qq音乐", rule=to_me(),priority=5)
@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想听什么歌呢？小可爱")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get(city)
    await weather.send(message=Message(city_weather))


async def get(city: str):
    cityname = city
    url = 'http://www.crys.top/api/netease.php?msg=%s&n=1&type=text'%cityname
    d = requests.get(url=url, timeout=5).text
    ur=re.findall('播放链接：(.*)',d)[0]
    # print(ur)
    ti=cityname
    # print(ti)
    tu=re.findall('±img=(.*?)±',d)[0]
    # print(tu)
    yinyue = f"[CQ:music,type=custom,audio={ur},title={ti},image={tu}]"
    return yinyue

