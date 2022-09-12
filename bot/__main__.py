import os
import math
import keep_alive
from random import randint
from time import sleep
from pyrogram import filters
from bot import sudo_users, app







@app.on_message(filters.command(["count"]))
def forward(client, message):
 if message.from_user.id in sudo_users:
      if len(message.command) > 1:
        chat_id = int(message.command[1])
        hisx = client.get_history_count(chat_id)
        client.send_message(chat_id=message.chat.id,
                        text=hisx)

@app.on_message(filters.command(["fwdx", "forwardx"]))
async def forward(client, message):
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
              msgx = await message.reply_text("Starting Bot")
            for i in range(len(listxz) & len(listxzx)):
              z = 4*(offset_id-listxz[i]+1)/60
              await msgx.edit_text('Total Messages: ' + str(offset_id-limit+1) + '\nMessage ID: ' + yts1 + '/' + str(listxz[i]) + '\nMessage No.: ' + str(listxzx[i]) + '\nRemaining: ' + str(offset_id-listxz[i]) + '\nEstimated Time: ' + str(math.trunc(z)) + ' minutes ' + str(int((z % 1)*60)) + ' seconds')
              sleep(randint(2,6))
              await client.copy_message(
            chat_id=to_id,
            from_chat_id=chat_id,
            message_id=listxz[i])
              await msgx.edit_text('Message ID: ' + str(listxz[i]) + '\nMessage No.: ' + str(listxzx[i]) + '\nMessage Copied Successfully')
            await msgx.edit_text(str(offset_id-limit+1) + ' Messages Copied Successfully\n\n' + 'Last Message ID : ' + str(yts1) + '/' + str(offset_id))
          except Exception as e:
              await message.reply_text(f"```{e}```")
        else:
          reply = await message.reply_text("```Invalid Chat Identifier. Give me a chat id.```")
          sleep(5)
          await reply.delete()
      else:
        reply = await message.reply_text("```Invalid Command ! Use /fwd {SourceChatID} {StartingMessageID} {LastMessageID} {TargetChatID}```")
        sleep(20)
        await reply.delete()


@app.on_message(filters.text)
async def send(bot, msg):
  data1 = msg.text
  if data1.startswith('https://t.me/c/'):
    data1_list = data1.replace("https://t.me/c/", "").split("/")
    user_id = msg.chat.id
    data2_ask = await bot.ask(user_id, f'ok, now give last message link or last message id.', filters=filters.text)
    data2 = str(data2_ask.text)
    try:
      data2_list = data2.replace("https://t.me/c/", "").split("/")
      data3 = f"/fwd -100{str(data1_list[0])} {str(data1_list[1])} {str(data2_list[1])} -1001615404314"
    except:
      data3 = f"/fwd -100{str(data1_list[0])} {str(data1_list[1])} {data2} -1001615404314"
    
    await bot.send_message(chat_id=user_id,
                        text=f"{str(data3)}")


keep_alive.keep_alive()
app.run()
