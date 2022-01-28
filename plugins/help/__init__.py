from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from ..power import power

help = on_command("菜单", rule=to_me(), priority=5)

@help.handle()
async def get_help(bot: Bot, event: Event , state: T_State):
    menu = await get_menu(help)
    await help.finish(menu)

async def get_menu(help: str) -> str:
    return f"操作方式：\n\
    ①输入“七海”后面加想要实现的事件，如：\n\
    七海，讲个笑话\n\
    ②直接@本QQ，后面加想要实现的事件，如：\n\
    @七海千秋，讲个笑话\n\
    目前已经完成的功能：\n\
    打招呼（你好），打招呼（晚安），签到，商店，来张美图（随机获得一张娜娜米的美图），天气查询，星座运势查询\n\
    注：天气查询和星座运势查询功能每天分别限制使用50次（因为屑作者没花钱去买QAQ）\n\
    如果使用某功能时提示\"还没有开机哦~请先开机！\"，请@管理开机"
