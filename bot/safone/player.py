import os
import re
import time
import ffmpeg
import asyncio
from os import path
from asyncio import sleep
from config import Config
from bot.safone.nopm import User
from youtube_dl import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pytgcalls import GroupCallFactory
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CHAT_ID = none
USERNAME = Config.BOT_USERNAME

STREAM = {6}
VIDEO_CALL = {}

ydl_opts = {
        "format": "best",
        "addmetadata": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "videoformat": "mp4",
        "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)
group_call_factory = GroupCallFactory(User, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)

@Client.on_message(filters.command(["stream", f"stream@{USERNAME}"]) & filters.group)
async def stream(client, m: Message):
    if 1 in STREAM:
        await m.reply_text( Type /endstream to Stop The Existing Stream!")
        return

    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await m.reply("Send Me A Live Stream Link / YouTube Video Link / Reply To A Video To Start Streaming!__")

    elif ' ' in m.text:
        msg = await m.reply_text("`Processing ...`")
        text = m.text.split(' ', 1)
        url = text[1]
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex,url)
        if match:
            await msg.edit(" `Starting YouTube Stream ...`")
            try:
                info = ydl.extract_info(url, False)
                ydl.download([url])
                ytvid = path.join("downloads", f"{info['id']}.{info['ext']}")
            except Exception as e:
                await msg.edit(f"YouTube Download Error! \n\n`{e}`")
                return
            await sleep(2)
            try:
                group_call = group_call_factory.get_group_call()
                await group_call.join(CHAT_ID)
                await group_call.start_video(ytvid)
                VIDEO_CALL[CHAT_ID] = group_call
                await msg.edit(f"▶Started [YouTube Streaming]({url})!")
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
            except Exception as e:
                await msg.edit(f"unable to play please recheck and play again \n\nError: `{e}`")
        else:
            await msg.edit("`Starting Live Stream ...`")
            live = url
            await sleep(2)
            try:
                group_call = group_call_factory.get_group_call()
                await group_call.join(CHAT_ID)
                await group_call.start_video(live)
                VIDEO_CALL[CHAT_ID] = group_call
                await msg.edit(f"▶Started [Live Streaming]({live})!")
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
            except Exception as e:
                await msg.edit(f"unable to play please recheck and play again \n\nError: `{e}`")
        else: \n\nError: `{e}`")

    elif media.video or media.document:
        msg = await m.reply_text(" `Downloading ...`")
        video = await client.download_media(media)
        await sleep(2)
        try:
            group_call = group_call_factory.get_group_call()
            await group_call.join(CHAT_ID)
            await group_call.start_video(video)
            VIDEO_CALL[CHAT_ID] = group_call
            await msg.edit("▶Started Streaming!")
            try:
                STREAM.remove(0)
            except:
                pass
            try:
                STREAM.add(1)
            except:
                pass
        except Exception as e:
            await msg.edit(f"unable to play please recheck and play again \n\nError: `{e}`")
        else: \n\nError: `{e}`")
    else:
        await m.reply_text("Send Me An Live Stream Link / YouTube Video Link / Reply To An Video To Start Streaming!")
        return


@Client.on_message(filters.command(["endstream", f"endstream@{USERNAME}"]) & filters.group)
async def endstream(client, m: Message):
    if 0 in STREAM:
        await m.reply_text("Please Start The Stream First!")
        return
    try:
        await VIDEO_CALL[CHAT_ID].stop()
        await m.reply_text("Stopped Streaming!")
        try:
            STREAM.remove(1)
        except:
            pass
        try:
            STREAM.add(0)
        except:
            pass
    except Exception as e:
        await m.reply_text(f"unable to play please recheck and play again \n\nError: `{e}`")
        else: \n\nError: `{e}`")


admincmds=["stream", "endstream", f"stream@{USERNAME}", f"endstream@{USERNAME}"]

@Client.on_message(filters.command(admincmds) & filters.group)
async def notforu(_, m: Message):
    k = await m.reply_text("thanks for choosing me")
    await sleep(5)
    await k.delete()
    try:
        await m.delete()
    except:
        pass

allcmd = ["start", "help", f"start@{USERNAME}", f"help@{USERNAME}"] + admincmds

@Client.on_message(filters.command(allcmd) & filters.group)
async def not_chat(_, m: Message):
    buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/EnglishChatting_Club"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/StylishUser"),
            ],
            [
                InlineKeyboardButton("OWNER", url="https://t.me/monstar_0"),
            ]
         ]
    await m.reply_text(text="Sorry, You Can't Use This Bot In This Group ")
