import datetime

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from database.database_connect import conn
# from __init__ import *

#解耦失败了……

shopping = on_command("商店", rule=to_me(), priority=5)
welcome = ["欢迎来到商店，这次想买些什么呢？"]
goods_dict = {"刨冰" : "2",
        "草饼":"4",
        "游戏卡带":"10",
        "游戏机":"50"}
for i,item in enumerate(goods_dict.items(),start=1):
    k,v =item
    welcome.append(f"{i}.{k.ljust(6,'　')}{v.rjust(4)}硬币")


@shopping.got("good",prompt="\n".join(welcome))            
@shopping.got("number",prompt="那么要买几个呢？")
async def handle_shopping(bot: Bot, event: Event, state: T_State):
    if state["good"] in goods_dict.keys():
        # print(goods_dict[state["good"]])
        # print(state["number"])
        cursor = conn.cursor()
        query_sql = cursor.execute('SELECT sum(currency) FROM nanami.daliy where qqnum={}'.format(event.get_user_id()))
        conn.commit()
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        total_price = int(goods_dict[state["good"]])*int(state["number"])
        if data_dict[0]["sum(currency)"]<total_price:
            await shopping.finish("现在没有这么多硬币……")
        else:
            spend = 0-total_price   
            shopping_sql = cursor.execute('insert into daliy(`qqnum`,`date`,`currency`)values({},\'{}\',{})'.format(event.get_user_id(), datetime.date.today(), spend))
            conn.commit()
            cursor.close()
            await shopping.finish("购买了{}*{}，花费{}枚硬币".format(state["good"], state["number"], total_price))
    