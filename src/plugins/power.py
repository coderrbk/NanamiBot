from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import Permission
# from __init__ import *

power_on = on_command("开机", rule=to_me(), priority=1)
power = [0]
@power_on.handle()
async def power_up(bot: Bot, event: Event):
    power[0] = 1
    await power_on.finish("已经开机了哦~")


power_off = on_command("关机", rule=to_me(), priority=1)
@power_off.handle()
async def power_down(bot: Bot, event: Event):
    power[0] = 0
    await power_off.finish("关机……Zzz…")