#  DeadLineTG - The example use of Pyrogram library and for learning
#  Copyright (C) 2022 DeadLine-Tech <https://github.com/vickysaputraa>
#
#  This file is part of DeadLineTG.
#
from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

bot = Client(
    "kyz@DeadLine",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    plugins=dict(root="deadline.plugins")
)

if __name__ == "__main__":
    bot.run()
