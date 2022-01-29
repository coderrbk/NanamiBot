import random

from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from nonebot.adapters.cqhttp import *
from nonebot.permission import SUPERUSER

shut_up = on_command("禁言我", rule=to_me(), priority=5)
set_admin = on_command("给我管理员", rule=to_me(), priority=5)
unset_admin =on_command("取消管理员", permission=SUPERUSER, rule=to_me(), priority=5)

@shut_up.handle()
async def shut_somebody_up(bot: Bot, event: MessageEvent, state: T_State):
    if await GROUP_ADMIN(bot, event):
        await shut_up.finish("呜……真的要禁言你吗？你可是管理员哎！")
    await bot.set_group_ban(group_id=718762916, user_id=event.get_user_id(), duration=300)
    await shut_up.finish("已经把{}禁言了啾".format(event.sender.card))

@set_admin.handle()
async def setadmin(bot: Bot, event: MessageEvent, state: T_State):
    if event.get_user_id() not in bot.config.superusers:
        await set_admin.finish("没有我哥哥的命令我是不会把管理员的权限给你的！")
    await bot.set_group_admin(group_id=718762916, user_id=event.get_user_id(), enable=True)
    await set_admin.finish("{}，给你管理员权限了哦".format(event.sender.card))

@unset_admin.handle()
async def unsetadmin(bot: Bot, event: MessageEvent, state: T_State):
    await bot.set_group_admin(group_id=718762916, user_id=event.get_user_id(), enable=False)
    await unset_admin.finish("现在 {} 已经不是管理员了啾".format(event.sender.card))