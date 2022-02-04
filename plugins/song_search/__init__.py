from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 

from .data_source import get_song

song_search = on_command("点歌", rule=to_me(), priority=5)

@song_search.handle()
async def songsearch(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["target_song"] = args



@song_search.got("target_song", prompt="嗯...想听什么歌呢？")
async def handle_songsearch(bot: Bot, event: Event, state: T_State):
    await song_search.send("正在搜索了哦…嗯…让我看看是不是这首歌呢…")
    result = await get_song(state["target_song"])
    if result!=-1:
        await song_search.finish(f"找到了！\n{result}")
    else:
        await song_search.finish("啊嘞？没有找到这首歌呢……试试输入更精确的描述或者换一个歌曲吧")