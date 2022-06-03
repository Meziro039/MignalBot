import datetime
from misskey import Misskey
import time

# [Config]
domain = "you-domain.dev"
token = ""
display = 12 # 12 or 24
timezone = "jst" # 現時点では利用不可
interval = 30 # 5 or 10 or 30 or 60
postdata = "{ja12}{hour}時{minute}分です。"
# [Config]

# Variable
msk = Misskey(domain, i=token) 
interval_set = [0]
postdata_set = "0"
dt_now = 0
year = 0
month = 0
day = 0
hour = 0
minute = 0
timezone_set = "0"
en12 = "0"
ja12 = "0"

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
        dt_now = datetime.datetime.now()
        if dt_now.minute in interval_set:
            break
        time.sleep(1)

    # 時間格納
    year = dt_now.year
    month = dt_now.month
    day = dt_now.day
    hour = dt_now.hour
    minute = dt_now.minute
    timezone_set = timezone

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
    postdata_set = postdata_set.replace('{timezone}', str(timezone_set))
    postdata_set = postdata_set.replace('{en12}', str(en12))
    postdata_set = postdata_set.replace('{ja12}', str(ja12))

    # 投稿
    note = msk.notes_create(postdata_set, visibility="home")
    print(note["createdNote"]["id"])
    time.sleep(60)

    # C/https://github.com/Meziro039