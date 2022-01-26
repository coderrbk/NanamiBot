import random

from nonebot import *
from nonebot.plugin import on_keyword
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
# from .power import power

hello_nanami = on_command("你好", rule=to_me(), priority=5)

@hello_nanami.handle()
async def hello(bot: Bot, event: Event, state: T_State):
    hellos = ["你好！我是七海千秋！","（咔哒）你好…（咔哒，咔哒咔哒…）","你好呀，请多指教~","呼啊（哈欠），你好","嗯？唔…你好","你好，要一起来玩游戏吗？嘿嘿（递游戏机）"]
    await hello_nanami.finish(hellos[random.randint(0,len(hellos)-1)])