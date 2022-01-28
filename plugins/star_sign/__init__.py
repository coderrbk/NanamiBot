from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 

from .data_source import get_star_sign

STAR_SIGN_LIST = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', 
                  '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']

star_sign = on_command("星座运势查询", rule=to_me(), priority=5)

@star_sign.handle()
async def query_star_sign(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["star_sign"] = args

@star_sign.got("star_sign", prompt="你想知道哪个星座的运势呢")
async def handle_city(bot: Bot, event: Event, state: T_State):
    query_star_sign = state["star_sign"]
    if query_star_sign not in STAR_SIGN_LIST:
        await star_sign.reject("{}？这是什么星座啊！快点告诉我你想要查什么星座啊喂！".format(query_star_sign))
    starsign = await get_star_sign(query_star_sign)
    await star_sign.finish(starsign)
