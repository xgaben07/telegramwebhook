import os
from telegram import Bot
from telegram.error import TelegramError

def send_message(data):
    try:
        tg_bot = Bot(token=os.environ['TOKEN'])
        channel = os.environ['CHANNEL']

        print('---> Sending message to telegram')
        tg_bot.send_message(
            chat_id=channel,
            text=data,
            parse_mode="MARKDOWN",
        )
        return True
    except KeyError:
        print('---> Key error - sending error to telegram')
    except TelegramError as te:
        print('---> Telegram Error:', te)
    except Exception as e:
        print('[X] Unexpected Error:\n>', e)
    return False
