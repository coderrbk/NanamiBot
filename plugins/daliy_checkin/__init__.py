
import datetime
import random

from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from nonebot.adapters.cqhttp import *
# from ..power import power
from database.database_connect import conn


hello_nanami = on_command("签到", rule=to_me(), priority=5)

@hello_nanami.handle()
async def hello(bot: Bot, event: Event, state: T_State):
    # if power[0]==1:
        cursor = conn.cursor()
        counter = 0
        currency = random.randint(10,20)
        favorvalue = random.randint(5,10)
        dt1 = datetime.date.today()
        select_sql = cursor.execute('select `qqnum`, `date` from nanami.daliy')
        conn.commit() 
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        print(data_dict)
        for d in data_dict:
            if str(d['qqnum']) == event.get_user_id():
                dt2 = d['date']
                sub = dt1-dt2
                if sub.days == 0:
                    counter=1
                    break
        try:
            if counter==0:
                insert_sql = cursor.execute('insert into nanami.daliy(`qqnum`, `date`, `currency`, `favorvalue`)values({},\'{}\',{},{});'.format(event.get_user_id(),dt1, currency, favorvalue))
                conn.commit()
                await hello_nanami.finish("签到成功！获得了{}枚硬币，七海对你的好感度增加了{}！".format(currency, favorvalue))
            else:
                await hello_nanami.finish("你今天已经签到过了哦~明天再来吧")
        finally:
            cursor.close() 
    # else:
        await hello_nanami.finish("还没有开机哦~请先开机！")