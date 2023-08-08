import os
from telegram import Bot


def sendMessage(data):
    tg_bot = Bot(token=os.environ.get('TOKEN'))
    channel = os.environ.get('CHANNEL')

    if not tg_bot:
        print("[X] Telegram bot token not found.")
        return False
    if not channel:
        print("[X] Telegram channel ID not found.")
        return False

    try:
        tg_bot.sendMessage(
            channel,
            data,
            parse_mode="MARKDOWN",
        )
        return True
    except Exception as e:
        print('[X] Unexpected Error:', type(e), e)
        return False
