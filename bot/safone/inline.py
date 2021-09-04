

import asyncio
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, errors
from config import Config

USERNAME = Config.BOT_USERNAME
REPLY_MESSAGE = Config.REPLY_MESSAGE

buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/EnglishChatting_Club"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/StylishUser"),
            ],
            [
                InlineKeyboardButton("owner", url="https://t.me/monstar_0"),
            ]
         ]

@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "monstar_0":
        answers.append(
            InlineQueryResultArticle(
                title="Deploy Own Video Player Bot",
                input_message_content=InputTextMessageContent(f"{REPLY_MESSAGE}\n\n<b>© Powered By : \n@monstar_0 | @tithonus </b>", disable_web_page_preview=True),
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return

__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
