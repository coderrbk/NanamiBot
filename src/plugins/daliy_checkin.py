import pymysql
import datetime
import random

from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from nonebot.adapters.cqhttp import *
# from .power import power



hello_nanami = on_command("签到", rule=to_me(), priority=5)

@hello_nanami.handle()
async def hello(bot: Bot, event: Event, state: T_State):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='nanami', charset='utf8')
    cursor = db.cursor()
    counter = 0
    currency = random.randint(10,20)
    favorvalue = random.randint(5,10)
    dt1 = datetime.date.today()
    print(dt1)
    select_sql = cursor.execute('select `qqnum`, `date` from nanami.daliy')
    db.commit() 
    desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
    data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]  # 列表表达式把数据组装起来
    print(data_dict)
    for d in data_dict:
        print(d['qqnum'])
        # print(type(d['qqnum']))
        # print(type(event.get_user_id()))
        print(str(d['qqnum']) == event.get_user_id())
        if str(d['qqnum']) == event.get_user_id():
            dt2 = d['date']
            print(dt2)
            sub = dt1-dt2
            # print(sub.days)
            if sub.days == 0:
                counter=1
                # print("签到过了")
                break
    if counter==0:
        insert_sql = cursor.execute('insert into nanami.daliy(`qqnum`, `date`, `currency`, `favorvalue`)values({},\'{}\',{},{});'.format(event.get_user_id(),dt1, currency, favorvalue))
        db.commit()
        cursor.close() 
        db.close()
        await hello_nanami.finish("签到成功！获得了{}枚硬币，七海对你的好感度增加了{}！".format(currency, favorvalue))
    else:
        cursor.close()
        db.close()
        await hello_nanami.finish("你今天已经签到过了哦~明天再来吧")
