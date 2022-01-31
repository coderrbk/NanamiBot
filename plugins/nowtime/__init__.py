import datetime

from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 
from nonebot import require

scheduler = require("nonebot_plugin_apscheduler").scheduler
@scheduler.scheduled_job("cron", hour="*", minute=0)
async def run_every_hour():
    driver = get_driver()
    BOT_ID = str(driver.config.bot_id)
    bot = driver.bots[BOT_ID]
    group_id="grout_id"
    # 你所想要实现的grout_id
    await bot.send_group_msg(group_id=group_id, message="整点报时！现在是{}点整".format(datetime.datetime.now().hour))

what_time_is_it_now = on_command("报时", rule=to_me(), priority=5)
@what_time_is_it_now.handle()
async def time_now(bot: Bot):
    await what_time_is_it_now.finish(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))