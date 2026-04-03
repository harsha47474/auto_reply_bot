from telethon import TelegramClient, events
import os
from dotenv import load_dotenv


load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
AUTO_REPLY_MSG = """<i>Hey there! 👋 This is an automated message.
Yuta is a little busy at the moment, but he'll get back to you as soon as he sees your text.
Thanks for your patience! 🙂</i>"""

client = TelegramClient('auto_reply_bot', API_ID, API_HASH)

replied_to = set()
print(replied_to)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_reply(event):
    sender = await event.get_sender()

    if sender.bot:
        return

    sender_id = sender.id

    if sender_id not in replied_to:
        await event.reply(AUTO_REPLY_MSG, parse_mode="html")
        replied_to.add(sender_id)
        print(f"Replied to {sender.first_name} (ID: {sender_id})")

print("Auto-reply bot is running...")
with client:
    client.run_until_disconnected()