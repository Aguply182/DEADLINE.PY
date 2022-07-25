from pyrogram import Client, filters
from pyrogram.types import Message
import time, asyncio, sys, os

version = '0.0.1-Dev'

@Client.on_message(filters.command("help", prefixes=['/', '!']) & filters.me)
async def help_msg(_, m: Message):
    await m.delete()
    reply = '**Commands** :'
    reply += '\n » /speed - checking speed'
    reply += '\n » /restart - restarting program'
    reply += '\n » /tagall - mention all members'
    reply += '\n\n© @DEADLINE_TECH.'
    await m.reply(reply)

@Client.on_message(filters.command("speed", prefixes=['/', '!']) & filters.me)
async def speed_msg(_, m: Message):
    start = time.time()
    await m.edit("**Benchmarking speed...**")
    await asyncio.sleep(1)
    await m.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await asyncio.sleep(1)
    await m.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await asyncio.sleep(1)
    await m.edit("**40% ████▒▒▒▒▒▒**")
    await asyncio.sleep(1)
    await m.edit("**60% ██████▒▒▒▒**")
    await asyncio.sleep(1)
    await m.edit("**80% ████████▒▒**")
    await asyncio.sleep(1)
    await m.edit("**100% ██████████**")
    await asyncio.sleep(2)
    end = time.time() - start
    await m.edit(f"{round(end, 2)} ms")

@Client.on_message(filters.command("restart", prefixes=['/', '!']) & filters.me)
async def restarting(_, m: Message):
    await m.delete()
    newevent = await m.reply("Restarting...")
    await newevent.delete()
    python = sys.executable
    os.execl(python, python, *sys.argv)

@Client.on_message(filters.command("tagall", prefixes=['/', '!']) & filters.me)
async def tagall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    string = "**Mention all :\n**"
    limit = 1
    icm = client.get_chat_members(chat_id)
for member in icm:
        if limit <= 5:
            string += f" » {member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string)
            limit = 1
            string = ""
            await asyncio.sleep(2)
