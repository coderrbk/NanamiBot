from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 

from .data_source import get_weather
from .citys import citylist

weather = on_command("天气查询", rule=to_me(), priority=5)

@weather.handle()
async def query_weather(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args

@weather.got("city", prompt="你想知道哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    if city not in citylist:
        await weather.reject("哎？有这个城市吗……？（试试换个城市输入）")
    city_weather = await get_weather(city)
    await weather.finish(city_weather)