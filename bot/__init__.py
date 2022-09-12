from pyrogram import Client

api_id = 8763712
api_hash = "835d27216f117e22a5c192b89a4ce457"
bot_token = "5310301280:AAGLExVt5XtDNM-N-shGt_hCYrRdftAhyQg"
tg_session = None
sudo_users = ["830785064", "872830003", "846709496", "927193767", "1542508017", "913846663", "983956963", "1700962147"]


if tg_session:
  app = Client(tg_session, api_id, api_hash)
elif bot_token:
  app = Client(":memory:", api_id, api_hash, bot_token=bot_token)
else:
  print('Give Token!')
  sys.exit(1)

with app:
  print('Bot Started!')
