from math import trunc
from random import randint, choices
from time import sleep
from time import time
from datetime import datetime, timedelta
from pytz import timezone
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import sudo_users, app, uname
import string


IST = timezone('Asia/Kolkata')

PROCESS = []

def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f'{days}d'
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f'{hours}h'
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f'{minutes}m'
    seconds = int(seconds)
    result += f'{seconds}s'
    return result

botStartTime = time()


@app.on_message(filters.command(["start"]))
async def startcmd(client, message):
        await client.send_message(chat_id=message.chat.id,
                                text=f'⚡Bot By Sahil Nolia')


@app.on_message(filters.command(["time"]))
async def timecmd(client, message):
  if message.from_user.id in sudo_users:
        currentTime = get_readable_time(time() - botStartTime)
        await client.send_message(chat_id=message.chat.id,
                                text=f'♻Bot Is Alive For {currentTime}')
  else:
        await client.send_message(chat_id=message.chat.id,
                                text=f"❌Only Authorized Users can use this command")


@app.on_message(filters.command(["help"]))
async def helpcmd(client, message):
        await client.send_message(chat_id=message.chat.id,
                                text='```Use /fwd {SourceChatID} {StartingMessageID} {LastMessageID} {TargetChatID}```')
  


@app.on_message(filters.command(["fwd"]))
async def forward(client, message):
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
              msgx = await message.reply_text("Starting Copying")
              TTL_MSG = str(offset_id-limit+1)
              nz1 = datetime.now()
              res = ''.join(choices(string.ascii_uppercase +
                             string.digits, k=5))
              cstring = str(message.from_user.id) + '-' + str(res)
              PROCESS.append(cstring)
              cxmsg_id = ''
            for i in range(len(listxz) & len(listxzx)):
                if cstring in PROCESS:
                    REM_MSGS = offset_id-listxz[i]
                    datetime_ist = datetime.now(IST)
                    TIMEZ = f"{datetime_ist.strftime('%I:%M:%S %p, %d %B %Y')}"
                    zm = 4 * (REM_MSGS+1) / (60 * 60)
                    hr = trunc(zm)
                    mint = trunc((zm % 1) * 60)
                    secs = trunc((((zm % 1) * 60) % 1) * 60)
                    tme = f"{hr}h{mint}m{secs}s"
                    after_time = datetime_ist + timedelta(seconds=secs, minutes=mint, hours=hr)
                    y_time = after_time.strftime('%I:%M:%S %p, %d %B %Y')
                    currentTime = get_readable_time(time() - botStartTime)
                    text = '🔄Remaining: ' + str(REM_MSGS) + '\n📎Total Messages: ' + TTL_MSG + '\n\n🆔COPYING_MSG: ' + yts1 + '/' + str(listxz[i]) + '\n🆔COPIED_MSG: ' + yts2 + '/' + str(cxmsg_id) + '\n🔢Message No: ' + str(listxzx[i]) + f'\n\n♻EST Completion Time: {str(y_time)}\n⌛EST Remaining Time: {str(tme)}\n\n❤Bot_Alive_Time : {currentTime}\n⌚Current_Time: {str(TIMEZ)}'
                    await msgx.edit_text(text=text,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌Cancel", callback_data=cstring)]]))
                    sleep(randint(2,6))
                    cx_msg = await client.copy_message(
                    chat_id=to_id,
                    from_chat_id=chat_id,
                    message_id=listxz[i])
                    cxmsg_id = cx_msg.id
                    text = '🔄Remaining: ' + str(REM_MSGS) + '\n📎Total Messages: ' + TTL_MSG + '\n\n🆔COPYING_MSG: ' + yts1 + '/' + str(listxz[i]) + '\n🆔COPIED_MSG: ' + yts2 + '/' + str(cxmsg_id) + '\n🔢Message No: ' + str(listxzx[i]) + f'\n\n♻EST Completion Time: {str(y_time)}\n⌛EST Remaining Time: {str(tme)}\n\n❤Bot_Alive_Time : {currentTime}\n⌚Current_Time: {str(TIMEZ)}'
                    await msgx.edit_text(text=text,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌Cancel", callback_data=cstring)]]))
                else:
                    nz2 = datetime.now()
                    duration = nz2 - nz1
                    zmx1= duration.total_seconds()
                    zmx = zmx1/(60 * 60)
                    hrx = trunc(zmx)
                    mintx = trunc((zmx % 1) * 60)
                    secsx = trunc((((zmx % 1) * 60) % 1) * 60)
                    ttlextime = f'{str(hrx)}h{str(mintx)}m{str(secsx)}s'
                    await msgx.delete()
                    text = '⛔ Cancelled By User' + '\n\n🆔MSG_ID_FROM: ' + yts1 + '/' + str(listxz[i]) + '\n\n🆔MSG_ID_TO: ' + yts2 + '/' + str(cxmsg_id) + f'\n\n⌛Total_Time: {str(ttlextime)}' + f'\n\n⌚Time: {str(TIMEZ)}'
                    await client.send_message(chat_id=message.chat.id,text=text)
                    return
            nz2 = datetime.now()
            duration = nz2 - nz1
            zmx1= duration.total_seconds()
            zmx = zmx1/(60 * 60)
            hrx = trunc(zmx)
            mintx = trunc((zmx % 1) * 60)
            secsx = trunc((((zmx % 1) * 60) % 1) * 60)
            ttlextime = f'{str(hrx)}h{str(mintx)}m{str(secsx)}s'
            await msgx.edit_text('✅' + TTL_MSG + ' Messages Copied Successfully\n\n' + '🆔MSG_ID_FROM: ' + yts1 + '/' + str(listxz[i]) + '\n\n🆔MSG_ID_TO: ' + yts2 + '/' + str(cxmsg_id) + f'\n\n⌛Time_Taken: {str(ttlextime)}' + f'\n\n⌚Time: {str(TIMEZ)}')
          except Exception as e:
              await message.reply_text(f"```{e}```")
        else:
          reply = await message.reply_text("```Invalid Chat Identifier.```")
          sleep(5)
          await reply.delete()
      else:
        reply = await message.reply_text("```Invalid Command ! Use /fwd {SourceChatID} {StartingMessageID} {LastMessageID} {TargetChatID}```")
        sleep(20)
        await reply.delete()


@app.on_message(filters.command(["fwdx"]))
async def send(bot, msg):
  if msg.from_user.id in sudo_users:
    try:
      user_id = msg.chat.id
      data2_ask = await bot.ask(user_id, f'Forward Starting Message From Source Chat', filters=filters.text)
      from_chat = data2_ask.forward_from_chat.id
      start_msg_id = data2_ask.forward_from_message_id
      data3_ask = await bot.ask(user_id, f'Forward Last Message From Source Chat', filters=filters.text)
      last_msg_id = data3_ask.forward_from_message_id
      data4_ask = await bot.ask(user_id, f'Forward A Message From Target Chat', filters=filters.text)
      to_chat = data4_ask.forward_from_chat.id
      await bot.send_message(chat_id=user_id,
                        text=f"`/fwd {str(from_chat)} {str(start_msg_id)} {str(last_msg_id)} {str(to_chat)}`")
    except Exception as e:
              await msg.reply_text(f"```{e}```")
              

@app.on_callback_query()
async def newbt(client, callback_query):
    if callback_query.message.chat.id in sudo_users:
        txt = callback_query.data
        if txt.startswith("YES"):
            txt = txt.replace('YES', '')
            try:
                PROCESS.remove(txt)
                chat_id = callback_query.message.chat.id
                message_id = callback_query.message.id
                await client.edit_message_text(chat_id=chat_id,
                                               message_id=message_id,
                                               text=f"✅Successfully Cancelled Forwarding!")
            except Exception as e:
              await client.send_message(chat_id=callback_query.message.chat.id,
                                    text=f"{e}")
        else:
            txt = f'YES{txt}'
            await client.send_message(chat_id=callback_query.message.chat.id,
                                    text=f"Are You Sure?",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌Yes 100% Sure! Cancel Forwarding.", callback_data=txt)]]))






print(f'⚡{uname} Bot Started Successfully!⚡')
app.run()
