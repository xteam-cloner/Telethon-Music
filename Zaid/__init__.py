import os

from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from pytgcalls import PyTgCalls
#from pytgcalls import compose
#from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


from Config import Config
BOT_USERNAME = Config.BOT_USERNAME
ASSISTANT_ID = Config.ASSISTANT_ID

bot = TelegramClient('Zaid', api_id=Config.API_ID, api_hash=Config.API_HASH)
Zaid = bot.start(bot_token=Config.BOT_TOKEN)
client = TelegramClient(StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH)
client.start()

class call_py:
    def __init__(self):
        self.calls = []

        for client in userbot.clients:
            pycall = PyTgCalls(
                client,
                cache_duration=100,
            )
            self.calls.append(pycall)

test_stream = 'http://docs.evostream.com/sample_content/assets/' \
              'sintel1m720p.mp4'
call_py(
e.chat.id,
    MediaStream(
        test_stream,
    ),
)
idle()
call_py.start()
