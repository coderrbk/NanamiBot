from nonebot import *
from nonebot.plugin import on, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from .power import power

import random


chat = on_command("聊天", rule=to_me(), priority=5)

@chat.handle()
async def get_chat(bot: Bot, event: Event , state: T_State):
    chats = ["“All to be nice.”一切都会好起来，好帅啊！","“El Psy Congroo.”凶真和助手之间的感情好奇妙啊！"]
    if power[0] == 1:
        await chat.finish(chats[random.randint(0,len(chats)-1)])
    else:
        await chat.finish("还没有开机哦~请先开机！")
