from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import datetime
from jieba import posseg

@on_command('你好')
async def hello(session: CommandSession):
    
    action = session.current_arg_text.strip()
    # if not action:
    #     action = (await session.aget(prompt='叫我有什么事吗？')).strip()
    #     # 如果用户只发送空白符，则继续询问
    #     while not action:
    #         action = (await session.aget(prompt='啊嘞？是我听错了吗……')).strip()
    action_report = await reply_of_action(action)
    await session.send(action_report)

async def reply_of_action(action: str) -> str:
    return f'你好！我是七海千秋！'

@on_command('报时', aliases=('几点了'))
async def what_time_is_it_now(session: CommandSession):
    action = session.current_arg_text.strip()
    action_report = await replytime_of_action(action)
    await session.send(action_report)

async def replytime_of_action(action: str) -> str:
    time = datetime.datetime.strftime(
        datetime.datetime.now()
        , '%H点%M分'
        )
    return f'现在是{time}'

# @on_natural_language(keywords={'报时'})
# async def _(session: NLPSession):
#     stripped_msg = session.msg_text.strip()
#     # 对消息进行分词和词性标注
#     words = posseg.lcut(stripped_msg)

#     city = None
#     # 遍历 posseg.lcut 返回的列表
#     for word in words:
#         # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
#         if word.word in '时间' or '几点了' or '报时':
#             # ns 词性表示地名
#             break

#     # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#     return IntentCommand(60.0, '报时')

async def Zzz(action: str) -> str:
    return f'Zzz……'

@on_command(' ', aliases=(''))
async def ignore(session: CommandSession):
    action = session.current_arg_text.strip()
    if not action:
        action = (await session.aget(prompt='叫我有什么事吗？')).strip()
    # 如果用户只发送空白符，则继续询问
    while not action:
        action = (await session.aget(prompt='啊嘞？是我听错了吗……')).strip()
    action_report = await Zzz(action)
    await session.send(action_report)
