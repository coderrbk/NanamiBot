from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 

help = on_command("菜单", rule=to_me(), priority=5)

@help.handle()
async def get_help(bot: Bot, event: Event , state: T_State):
    menu = await get_menu(help)
    test = str(event.get_message())
    print(test)
    await help.finish(menu)

async def get_menu(help: str) -> str:
    return f"这里是菜单！"
