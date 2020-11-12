#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors.exceptions import UserIsBlocked
from bot import (
    AUTH_CHANNEL,
    BAN_COMMAND,
    BOT_WS_BLOCKED_BY_USER,
    COMMM_AND_PRE_FIX,
    DERP_USER_S_TEXT,
    START_COMMAND,
    UN_BAN_COMMAND
)
from bot.hf.fic import vhkzuoi_repliz_handler
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.hf.gfi import (
    get_file_id
)
from bot.sql.users_sql import (
    get_user_id
)


@Client.on_message(
    ~filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    ~filters.command(BAN_COMMAND, COMMM_AND_PRE_FIX) &
    ~filters.command(UN_BAN_COMMAND, COMMM_AND_PRE_FIX) &
    uszkhvis_chats_ahndler([AUTH_CHANNEL]) &
    vhkzuoi_repliz_handler
)
async def on_pm_s(client: Client, message: Message):
    user_id, reply_message_id = get_user_id(
        message.reply_to_message.message_id
    )
    try:
        await send_message_to_user(
            client,
            message,
            user_id,
            reply_message_id
        )
    except UserIsBlocked:
        await message.reply_text(BOT_WS_BLOCKED_BY_USER)


async def send_message_to_user(
    client: Client,
    message: Message,
    user_id: int,
    reply_message_id: int
):
    # 🥺 check two conditions 🤔🤔
    if message.media:False

            
