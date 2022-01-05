from random import randint, random
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp.message import Message
from .power import power

NUMBER_OF_PICTURES = 10
# 图片总数

meitu = on_command("来张美图", rule=to_me(), priority=5)

@meitu.handle()
async def text2(bot: Bot, event: Event , state: T_State):
    if power[0]==1:
        cq = "[CQ:image,file="+str(randint(6,NUMBER_OF_PICTURES))+".jpg,id=40000]"
        await meitu.finish(Message(cq))
    else:
        await meitu.finish("还没有开机哦~请先开机！")

# 使用cq码发送图片