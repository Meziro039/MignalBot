from misskey import Misskey
from NowTime import nowtime
import time

# [Config]
domain = "you-domain.dev"
token = ""
display = 12 # 12 or 24
timezone = "jst"
interval = 5 # 5 or 10 or 30 or 60
postdata = "{year}年{month}月{day}日{ja12}{hour}時{minute}分({timezone})です。"
# [Config]

# Variable
msk = Misskey(domain, i=token) 
interval_set = None
postdata_set = None
nt = None
year = None
month = None
day = None
hour = None
minute = None
timezone_set = None
en12 = None
ja12 = None

# コンフィグの設定
if 5 == interval:
    interval_set = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
if 10 == interval:
    interval_set = [0, 10, 20, 30, 40, 50]
if 30 == interval:
    interval_set = [0, 30]
if 60 == interval:
    interval_set = [0]

# main
while True:
    # 時間一致判定
    while True:
        nt = nowtime.get
        if nt(timezone, "minute") in interval_set:
            break
        else:
            time.sleep(1)

    # 時間格納
    year = nt(timezone, "year")
    month = nt(timezone, "month")
    day = nt(timezone, "day")
    hour = nt(timezone, "hour")
    minute = nt(timezone, "minute")

    # 12h表示判定
    if display == 12:
        if 12 <= hour:
            hour = hour - 12
            en12 = "PM"
            ja12 = "午後"
        else:
            en12 = "AM"
            ja12 = "午前"


    # データ処理
    postdata_set = postdata
    postdata_set = postdata_set.replace('{year}', str(year))
    postdata_set = postdata_set.replace('{month}', str(month))
    postdata_set = postdata_set.replace('{day}', str(day))
    postdata_set = postdata_set.replace('{hour}', str(hour))
    postdata_set = postdata_set.replace('{minute}', str(minute))
    postdata_set = postdata_set.replace('{timezone}', str(timezone.upper()))
    postdata_set = postdata_set.replace('{en12}', str(en12))
    postdata_set = postdata_set.replace('{ja12}', str(ja12))

    # 投稿
    note = msk.notes_create(postdata_set, visibility="home")
    print("NotePost: " + note["createdNote"]["id"])
    time.sleep(120)

# C/https://github.com/Meziro039