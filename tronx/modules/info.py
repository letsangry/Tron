import os

from pyrogram.types import Message

from tronx import app, CMD_HELP

from tronx.helpers import (
	gen,
	error,
	types,
	send_edit,
)




CMD_HELP.update(
	{"info" : (
		"info",
		{
		"minfo [reply to media]" : "Check media info including text information.", 
		"chatinfo" : "Get chats information."
		}
		)
	}
) 




@app.on_message(gen("minfo"))
async def media_info(_, m: Message):
	replied = m.reply_to_message
	if not replied:
		return await send_edit(
			m, 
			"Please reply to some media to get media info ..."
			)
	if types(m) == "photo":
		pie = replied.photo
		msg = "**Type:** Photo\n"
		msg += f"**Width:** `{pie.width}`\n"
		msg += f"**Height:** `{pie.height}`\n"
		msg += f"**Size:** `{pie.file_size}`\n"
		msg += f"**Date:** `{pie.date}`\n"
		if replied.caption:
			msg += f"**Caption:** `{replied.caption}`\n"
		else:
			msg += " "
		await send_edit(
			m, 
			"**⚶ Media Information ⚶**\n\n" + msg,
			parse_mode = "markdown"
			)
	elif types(m) == "video":
		pie = replied.video
		msg = "**Types:** Video\n"
		msg += f"**Width:** `{pie.width}`\n"
		msg += f"**Height:** `{pie.height}`\n"
		msg += f"**Duration:** `{pie.duration}`\n"
		msg += f"**Mime type:** `{pie.mime_type}`\n"
		msg += f"**Size:** `{pie.file_size}`\n"
		msg += f"**Streamable:** `{pie.supports_streaming}`\n"
		msg += f"**Date:** `{pie.date}`\n"
		if replied.caption:
			msg += f"**Caption:** `{replied.caption}`\n"
		else:
			msg +=  " "
		await send_edit(
			m, 
			"**⚶ Media Information ⚶**\n\n" + msg,
			parse_mode = "markdown"
			)
	elif types(m) == "sticker":
		pie = replied.sticker
		msg = "**Types:** sticker\n"
		msg += f"**File name:** `{pie.file_name}`\n"
		msg += f"**Width:** `{pie.width}`\n"
		msg += f"**Height:** `{pie.height}`\n"
		msg += f"**Mime type:** `{pie.mime_type}`\n"
		msg += f"**Size:** `{pie.file_size}`\n"
		msg += f"**Emoji:** `{pie.emoji}`\n"
		msg += f"**Animated:** `{pie.is_animated}`\n"
		msg += f"**Set name:** `{pie.set_name}`\n"
		msg += f"**Date:** `{pie.date}`\n"
		if replied.caption:
			msg += f"**Caption:** `{replied.caption}`\n"
		else:
			msg +=  " "
		await send_edit(
			m, 
			"**⚶ Media Information ⚶**\n\n" + msg,
			parse_mode = "markdown"
			)
	elif types(m) == "document":
		pie = replied.document
		msg = "**Types:** Document\n"
		msg += f"**File name:** `{pie.file_name}`\n"
		msg += f"**Mime type:** `{pie.mime_type}`\n"
		msg += f"**Size:** `{pie.file_size}`\n"
		msg += f"**Date:** `{pie.date}`\n"
		if replied.caption:
			msg += f"**Caption:** `{replied.caption}`\n"
		else:
			msg +=  " "
		await send_edit(
			m, 
			"**⚶ Media Information ⚶**\n\n" + msg,
			parse_mode = "markdown"
			)
	elif types(m) == "animation":
		pie = replied.animation
		msg = "**Types:** Animation\n"
		msg += f"**File name:** `{pie.file_name}`\n"
		msg += f"**Width:** `{pie.width}`\n"
		msg += f"**Height:** `{pie.height}`\n"
		msg += f"**Duration:** `{pie.duration}`\n"
		msg += f"**Mime type:** `{pie.mime_type}`\n"
		msg += f"**Size:** `{pie.file_size}`\n"
		msg += f"**Date:** `{pie.date}`\n"
		if replied.caption:
			msg += f"**Caption:** `{replied.caption}`\n"
		else:
			msg +=  " "
		await send_edit(
			m, 
			"**⚶ Media Information ⚶**\n\n" + msg,
			parse_mode = "markdown"
			)
	elif types(m) == "audio":
		pie = replied.audio
		msg = "**Types:** Audio\n"
		msg += f"**Title:** `{pie.title}`\n"
		msg += f"**Performer:** `{pie.performer}`\n"
		msg += f"**File name:** `{pie.file_name}`\n"
		msg += f"**Duration:** `{pie.duration}`\n"
		msg += f"**Mime type:** `{pie.mime_type}`\n"
		msg += f"**Size:** `{pie.file_size}`\n"
		msg += f"**Date:** `{pie.date}`\n"
		if replied.caption:
			msg += f"**Caption:** `{replied.caption}`\n"
		else:
			msg +=  " "
		await send_edit(
			m, 
			"**⚶ Media Information ⚶**\n\n" + msg,
			parse_mode = "markdown"
			)
	elif types(m) == "text":
		msg = "**Types:** Text\n"
		msg += f"**Text:** `{replied.text}`\n"
		await send_edit(
			m, 
			"**⚶ Text Information ⚶**\n\n" + msg,
			parse_mode = "markdown"
			)




@app.on_message(gen("chatinfo"))
async def get_chatinfo(_, m: Message):
	try:
		if len(m.command) > 1:
			chat_u = m.command[1]
			chat = await app.get_chat(chat_u)
		else:
			if m.chat.type == "private":
				await send_edit(m, "Please use it in groups or use .chatinfo [group username or id]")
				return
			else:
				chat_v = m.chat.id
				chat = await app.get_chat(chat_v)
	
		await send_edit(m, "Processing ...")
		neel = chat.permissions
		data = "**Chat Info:**\n\n"
		data += f"**Title:** `{chat.title}`\n"
		data += f"**Chat Id:** `{chat.id}`\n"
		data += f"**Chat Type:** `{chat.type}`\n"
		data += f"**Dc Id:** `{chat.dc_id}`\n"
		if chat.username:
			data += f"**Username:** `@{chat.username}`\n"
		else:
			None
		data += f"**Members:** `{chat.members_count}`\n"
		data += f"**Description:** `{chat.description}`\n"
		data += f"**Permissions:**\n\n"
		data += f"**Send Messages:** `{neel.can_send_messages}`\n"
		data += f"**Send Media:** `{neel.can_send_media_messages}`\n"
		data += f"**Send Stickers:** `{neel.can_send_stickers}`\n"
		data += f"**Send Animations:** `{neel.can_send_animations}`\n"
		data += f"**Send Games:** `{neel.can_send_games}`\n"
		data += f"**Inline Bots:** `{neel.can_use_inline_bots}`\n"
		data += f"**Web Page Preview:** `{neel.can_add_web_page_previews}`\n"  
		data += f"**Send Polls:** `{neel.can_send_polls}`\n"
		data += f"**Change Group Info:** `{neel.can_change_info}`\n"
		data += f"**Invite Users:** `{neel.can_invite_users}`\n"
		data += f"**Pin Messages:** `{neel.can_pin_messages}`\n"
		if data:
			await send_edit(m, data)
		else:
			await send_edit(
				m, 
				"Failed to get information of this group ..."
				)
	except Exception as e:
		await error(m, e)