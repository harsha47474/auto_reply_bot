# 🤖 — Telegram Auto-Reply Bot

A simple Python bot that automatically replies to people who 
DM you on Telegram when you're busy!

## Features
- 💬 Auto-replies to personal DMs only
- 🚫 Ignores group messages and bots
- 📝 Remembers who it already replied to (no spam)
- 💾 Persists replied list even after restart
- ✍️ Italic formatted message for a clean look

## Tech Stack
- Python
- Telethon
- python-dotenv

## Setup

1. Clone the repo
2. Install dependencies
   pip install telethon python-dotenv
3. Create a .env file
   API_ID=your_api_id
   API_HASH=your_api_hash
   PHONE=+91XXXXXXXXXX
4. Run it
   python auto_reply.py

## Note
Built for personal use only. Not for spamming!

## Author
Made by Harsha
