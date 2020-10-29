from pyrogram import Client
from config import api_id, api_hash
from pyrogram.errors import FloodWait
import time

app = Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash
)

app.start()

print("Количество сообщений:")
for dialog in app.iter_dialogs():
    try:
        count_messages = app.get_history_count(dialog.chat.id)
    except FloodWait as e:
        print("Перекур, телега не вечная...")
        print("Ждём {} секунд....".format(e.x))
        time.sleep(e.x)
    if dialog.chat.title:
        print("{} - {}".format(dialog.chat.title, count_messages))
    else:
        print("{} - {}".format(dialog.chat.username, count_messages))
