import random

from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
# from .power import power


goodnight = on_command("晚安", rule=to_me(), priority=5)

@goodnight.handle()
async def goodnight(bot: Bot, event: Event, state: T_State):
    goodnights = ["（七海按下了暂停键）哎，你要休息了吗，我一会就休息了哦，晚安","这么晚了呢，你也要好好休息，晚安~","哈~啊（打哈欠），好困…晚安","明天再尝试通关吧，晚安！"]
    # await goodnight3.finish(jokes[num])
    await goodnight.finish(goodnights[random.randint(0,len(goodnights)-1)])
