from nonebot import on_command
from nonebot.adapters.cqhttp import Event
from nonebot.adapters.cqhttp import Bot, Message
import time, requests
from nonebot.rule import to_me
weather = on_command("黄历", rule=to_me(),priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    msg = await xin()
    await weather.send(Message(msg))


async def xin():
    t = time.strftime("%Y-%m-%d", time.localtime())
    url = 'http://v.juhe.cn/laohuangli/d?date=%s&key=300e07021f3c31998962fc0c7ff229d7' % str(t)
    d = requests.get(url=url).json()
    yang = '阳历：' + d['result']['yangli']
    yin = '阴历：' + d['result']['yinli']
    wu = '五行：' + d['result']['wuxing']
    chong = '凶煞：' + d['result']['chongsha']
    bai = '拜祭：' + d['result']['baiji']
    j = '吉神：' + d['result']['jishen']
    yi = '宜：' + d['result']['yi']
    xiong = '凶神：' + d['result']['xiongshen']
    ji = '忌:' + d['result']['ji']
    return str(yang + '\n' + yin + '\n' + wu + '\n' + chong + '\n' + bai + '\n' + j + '\n' + yi + '\n' + xiong + '\n' + ji)
