from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
# matcher = on_keyword({"主人"})
matcher=on_command('主人',rule=to_me(),priority=5)

@matcher.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await matcher.send('我主人是川川大帅哥')


test = on_keyword({"test"})


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
    # biaoqing=f"[CQ:face,id=123]"#表情包使用
    # hongbao=f"[CQ:gift,qq={id},id=8]"#礼物使用
    await test.send(MessageSegment.at(id) + '你好帅哥')


test = on_keyword({"礼物", '我要礼物', '我也要礼物'})
# test=on_command('礼物',rule=to_me(),priority=5)

@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
    # biaoqing=f"[CQ:face,id=123]"#表情包使用
    hongbao = f"[CQ:gift,qq={id},id=0]"  # 礼物使用
    await test.send(MessageSegment.at(id) + hongbao)


# test=on_keyword({'笑'})
test = on_command('笑',rule=to_me())

@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # biaoqing = f"[CQ:face,id=182]"  # 表情包使用
    # await test.send(MessageSegment.at(id) + biaoqing + '哈哈，笑死我了')
    await test.send(MessageSegment.at(id) +MessageSegment.face(182)+'笑死我了')


# test=on_keyword({'哭'})
test = on_command('哭',rule=to_me())


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqing = f"[CQ:face,id=5]"  # 表情包使用
    await test.send(MessageSegment.at(id) + biaoqing + '呜呜，我真的哭了')


# test = on_keyword({'随机音乐'})
test=on_command('随机音乐',rule=to_me(),priority=5)

@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    url='https://api.paugram.com/acgm/'
    resp = requests.get(url).json()
    ge = resp.get('link')
    # print(ge)
    pic=resp.get('cover')
    # print(pic)
    ming=resp.get('title')
    # print(ming)
    # ci=resp.get('lyric')
    yinyue = f"[CQ:music,type=custom,audio={ge},title={ming},image={pic}]"
    await test.send(Message(yinyue))


test = on_keyword({'红包'})


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    biaoqing = f"[CQ:redbag,title=恭喜发财]"  # 表情包使用
    await test.finish(Message(biaoqing))


test = on_keyword({'戳'})


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # mes = str()
    chuo = f"[CQ:poke,qq={id}]"
    await test.send(Message(chuo))

# ceshi=on_keyword({'测试'})
# @ceshi.handle()
# async def h(bot: Bot, event: Event, state: T_State):
#     shi='http://cdn.video.picasso.dandanjiang.tv/59a7b0d30422084ff04896f1.mp4?sign=c83dd6238ff6fadf01b16e2b7a9e2e8a&t=60782bff'
#     pin= f"[CQ:video,file={shi}]"
#     await ceshi.send(Message(pin))