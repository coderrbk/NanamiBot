from logging import exception
from sqlite3 import Cursor, connect
import nonebot
import pymysql
import sys
from nonebot import *
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event 

driver=nonebot.get_driver()
__DATABASE = "mysql"
__DB_DRIVER = "pymysql"
__DB_USER = "root"
__DB_PASSWORD = "root"
__DB_HOST = "127.0.0.1"
__DB_PORT = 3306
__DB_NAME = "nanami"
__DB_CHARSET = "utf8"
try:
    conn = pymysql.connect(host=__DB_HOST , port=__DB_PORT, user=__DB_USER, passwd=__DB_PASSWORD, db=__DB_NAME, charset=__DB_CHARSET)
except Exception as e:
    nonebot.logger.opt(colors=True).critical(f"<r>数据库连接失败</r>, error: {repr(e)}")
    sys.exit(f"数据库连接失败, {e}")

@driver.on_startup
async def linktomysql():
    try:
        cursor = conn.cursor()
        sql = "select * from daliy"
        execute = cursor.execute(sql)
        cursor.close()
        nonebot.logger.opt().success(f"数据库连接完成")
    except Exception as e:
        nonebot.logger.opt(colors=True).critical(f"<r>数据库连接失败</r>, error: {repr(e)}")
        sys.exit(f"数据库连接失败, {e}")

@driver.on_shutdown
async def linkclose():
    conn.close()