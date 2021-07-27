"""
作者：yanghanwen
时间：2021/5/5
"""
from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests, re
from aiocqhttp.exceptions import Error as CQHttpError

yulu = on_keyword({'涩图'},priority=10)
@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await mei()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass

#这个网址已经失效了，需要新的插件加群:970353786
async def mei():
    url = 'https://api.66mz8.com/api/rand.img.php?type=美女&format=json'
    resp = requests.get(url)
    data = resp.json()
    ur = data.get('pic_url')
    tu = f"[CQ:image,file={ur}]"
    return tu
