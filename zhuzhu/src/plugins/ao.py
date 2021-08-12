# coding=utf-8
"""
作者：川川
时间：2021/8/2
"""
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
import requests

ao=on_keyword({'奥运'})
@ao.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await ao.send(message=Message(msg))

    except CQHttpError:
        pass

async def ji():
    url = 'https://api.cntv.cn/olympic/getOlyMedals'
    params = {
        'serviceId': 'pcocean',
        'itemcode': 'GEN-------------------------------',
    }

    json = requests.get(url, params=params).json()

    # print(json)
    r= json['data']['medalsList']
    # print(r)
    # for r in result[0:6]:
    #     return str(['rank']+r['countryname'].ljust(10))+str('金:')+ str(r['gold']+str('银:') + r['silver']+str('铜:') + r['bronze']+str('总:') + r['count'])
    return (r[0]['rank']+r[0]['countryname'].ljust(10)+'金' +str(r[0]['gold'])+ '银' + str(r[0]['silver'])+'铜' + str(r[0]['bronze'])+'总:' + str(r[0]['count'])+'\n'+r[1]['rank']+r[1]['countryname'].ljust(10)+'金' +str(r[1]['gold'])+ '银' + str(r[1]['silver'])+'铜' + str(r[1]['bronze'])+'总' + str(r[1]['count'])+'\n'+r[2]['rank'] +r[2]['countryname'].ljust(10) + '金' + str(r[2]['gold']) + '银' + str(r[2]['silver']) + '铜' + str(r[2]['bronze']) + '总' + str(r[2]['count']))

