from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from .power import power

help = on_command("菜单", rule=to_me(), priority=5)

@help.handle()
async def get_help(bot: Bot, event: Event , state: T_State):
    if power[0] == 1:
        menu = await get_menu(help)
        await help.finish(menu)
    else:
        await help.finish("还没有开机哦~请先开机！")

async def get_menu(help: str) -> str:
    return f"操作方式：\n\
    ①输入“七海”后面加想要实现的事件，如：\n\
    七海，讲个笑话\n\
    ②直接@本QQ，后面加想要实现的事件，如：\n\
    @七海千秋，讲个笑话"
