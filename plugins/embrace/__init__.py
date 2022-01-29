import random

from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from nonebot.adapters.cqhttp import *
from nonebot.permission import SUPERUSER

embrace = on_command("抱抱",rule=to_me(),priority=5)

@embrace.handle()
async def hug(bot: Bot, event: MessageEvent, state: T_State):
    message = await bot.get_group_member_info(group_id=718762916, user_id=event.get_user_id(), no_cache=True)
    if message["sex"]=="male":
        await embrace.finish("你是男生吧，日向同学告诉我不要随便和男生抱抱哦")
    if message["sex"]=="female":
        await embrace.finish("抱抱……好温暖……"+Message("[CQ:image,file=baobao.jpg,id=40000]"))
