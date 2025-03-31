import os
import logging

from telethon import TelegramClient, events
from telethon.sessions import StringSession
from pytgcalls import idle
from pytgcalls import PyTgCalls

from Config import Config

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

BOT_USERNAME = Config.BOT_USERNAME
ASSISTANT_ID = Config.ASSISTANT_ID

# Bot Client
bot = TelegramClient("Zaid", Config.API_ID, Config.API_HASH).start(
    bot_token=Config.BOT_TOKEN
)

# Assistant Client for PyTgCalls
assistant = TelegramClient(
    StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH
)

# PyTgCalls Client
call_py = PyTgCalls(assistant)


async def start_clients():
    """Starts both the bot and assistant clients."""
    try:
        await assistant.start()
        await call_py.start()
        logging.info("Bot and Assistant clients started successfully.")
    except Exception as e:
        logging.error(f"Failed to start clients: {e}")
