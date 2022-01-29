
import random

from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from nonebot.adapters.cqhttp import *

game = on_command("玩游戏", rule=to_me(), priority=5)

@game.handle()
async def games(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        game_choose = args.split()
        state["game"] = game_choose[0]

@game.got("game", prompt="你想玩哪个游戏呢？\n\
                    猜拳")
@game.got("quan", prompt="让我想想我要出什么……好了，出拳吧！\n（输入 剪刀/石头/布/不玩了）")
async def play_game(bot: Bot, event: MessageEvent, state: T_State):
    gamelist = ["猜拳"]
    if state["game"] == "猜拳":
        quan_list = ["石头","剪刀","布","不玩了"]
        if str(event.get_message()).strip() not in quan_list:
            # await game.send("让我想想我要出什么……好了，出拳吧！（输入 剪刀/石头/布/不玩了）")
            await game.reject("啊嘞？猜拳里有 {} 吗？".format(str(event.get_message()).strip()))
        userquan = str(event.get_message()).strip()
        if userquan =="不玩了":
            await game.finish("哎？不玩了吗？")
        qihaiquan = quan_list[random.randint(0,2)]
        await game.send("嗯…我出"+qihaiquan)
        if (qihaiquan =="石头" and userquan =="布") or\
            (qihaiquan =="剪刀" and userquan =="石头") or\
            (qihaiquan =="布" and userquan =="剪刀"):
            await game.reject("是{}赢了呢，不过我不会气馁的，再来吗？".format(event.sender.card))
        if (qihaiquan =="石头" and userquan =="剪刀") or\
            (qihaiquan =="剪刀" and userquan =="布") or\
            (qihaiquan =="布" and userquan =="石头"):
            await game.reject("我赢了，好开心~要再来吗？")
        if qihaiquan == userquan:
            await game.reject("诶，我们出的拳一样呢！难道你会读心术吗？嗯…再来吗？")