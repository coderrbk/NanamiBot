import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
# nonebot.load_plugins("src/plugins")
# nonebot.load_plugin("src/plugins/nonebot_plugin_strman")
# nonebot.load_plugins("src/plugins/foo")
nonebot.load_plugins("plugins")
nonebot.load_plugins("database")
# 加载插件目录
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()

nonebot.init(apscheduler_autostart=True)
nonebot.init(apscheduler_config={
    "apscheduler.timezone": "Asia/Shanghai"
})

if __name__ == "__main__":
    nonebot.run()