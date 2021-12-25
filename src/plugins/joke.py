from nonebot import *
from nonebot.plugin import on_keyword
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import random

jokes =["小明有一个同学跑步每次都拿第一，\n小明就问他：“你为什么每次都跑的那么快呢？”，\n同学说：“我最不喜欢跑步了。”，\n“那你还每次都跑第一？”，\n“这样我就可以每次跑完在终点线那看着你们跑啊。”","有一天，领导在台上讲话：“未来你们会成为形形的人！”，\n台下有人问：“不是形形色色的人吗？”，\n领导说：“不可以色色！”","“贵宾犬的英文是？”\n“VIP dog” ","狛枝生病住院了，同学们去看他。\n病床前二大问：“医生怎么说？”\n狛枝：“doctor。”"]
joke = on_keyword("笑话", rule=to_me(), priority=5)

@joke.handle()
async def have_a_joke(bot: Bot, event: Event):
    num = random.randint(0,len(jokes)-1)
    await joke.finish(jokes[num])