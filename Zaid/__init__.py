import os
import logging

from telethon import TelegramClient, events
from telethon.sessions import StringSession
import pytgcalls

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
        raise

async def main():
    """Main function to start clients and keep the bot running."""
    try:
        await start_clients()
        # Add your bot's event handlers and logic here.
        logging.info("Bot is running...")
        await bot.run_until_disconnected()
    except KeyboardInterrupt:
        logging.info("Bot stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        try:
            await call_py.stop()
            await assistant.disconnect()
            await bot.disconnect()
            logging.info("Clients disconnected.")
        except Exception as e:
            logging.error(f"Error during disconnection: {e}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
