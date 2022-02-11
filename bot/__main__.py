import os
import math
import keep_alive
from random import randint
from time import sleep
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, \
                remove_strings, replace_string, sudo_users


@app.on_message(filters.command(["count"]), group=1)
def forward(client, message):
 if message.from_user.id in sudo_users:
      if len(message.command) > 1:
        chat_id = int(message.command[1])
        hisx = client.get_history_count(chat_id)
        client.send_message(chat_id=message.chat.id,
                        text=hisx)

@app.on_message(filters.command(["fwd", "forward"]), group=1)
def forward(client, message):
 if message.from_user.id in sudo_users:
      if len(message.command) > 1:
        chat_id = int(message.command[1])
        if chat_id:
          try:
            offset_id = 0
            limit = 0
            if len(message.command) > 2:
              limit = int(message.command[2])
            if len(message.command) > 3:
              offset_id = int(message.command[3])
            if len(message.command) > 4:
              to_id = int(message.command[4])
              yts1 = message.command[1].replace("-100", "https://t.me/c/")
              yts2 = message.command[4].replace("-100", "https://t.me/c/")
              listxzx = list(range(1, offset_id-limit+2))
              listxz = list(range(limit, offset_id+1))
              msgx = message.reply_text("Starting Bot")
            for i in range(len(listxz) & len(listxzx)):
              z = 4*(offset_id-listxz[i]+1)/60
              msgx.edit_text('Total Messages: ' + str(offset_id-limit+1) + '\nMessage ID: ' + yts1 + '/' + str(listxz[i]) + '\nMessage No.: ' + str(listxzx[i]) + '\nRemaining: ' + str(offset_id-listxz[i]) + '\nEstimated Time: ' + str(math.trunc(z)) + ' minutes ' + str(int((z % 1)*60)) + ' seconds')
              sleep(randint(2,6))
              client.copy_message(
            chat_id=to_id,
            from_chat_id=chat_id,
            message_id=listxz[i])
              msgx.edit_text('Message ID: ' + str(listxz[i]) + '\nMessage No.: ' + str(listxzx[i]) + '\nMessage Copied Successfully')
            msgx.edit_text(str(offset_id-limit+1) + ' Messages Copied Successfully\n\n' + 'Last Message ID : ' + str(yts1) + '/' + str(offset_id))
          except Exception as e:
              message.reply_text(f"```{e}```")
        else:
          reply = message.reply_text("```Invalid Chat Identifier. Give me a chat id.```")
          sleep(5)
          reply.delete()
      else:
        reply = message.reply_text("```Invalid Command ! Use /fwd {SourceChatID} {StartingMessageID} {LastMessageID} {TargetChatID}```")
        sleep(20)
        reply.delete()
 else:
    client.send_message(chat_id=message.chat.id,
                        text=f"You are not authorized.")


keep_alive.keep_alive()
app.run()
