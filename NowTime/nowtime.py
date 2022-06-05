import datetime

# 変数の定義
    # 時刻に関する変数
dt_now = None
year = None
month = None
day = None
hour = None
minute = None
second = None
    # 処理に使う変数
tz_set_nt = None  # タイムゾーン設定
filter_nt = None  # フィルター設定
offset_which = None  # オフセットの方向(plus or minus)
offset_hour = None  # オフセット値格納(時)
offset_min = None  # オフセット値格納(分)
month_size = None  # 毎月の最大日数
uruu = None  # うるう年判定値の格納(y or n)
output = None  # 出力の格納

def get(tz_set_nt=None, filter_nt=None):

    # グローバル宣言
    global output

    def change():

        # グローバル宣言
        global output

        # 変数の設定
        dt_now = datetime.datetime.now(datetime.timezone.utc)
        year = dt_now.year
        month = dt_now.month
        day = dt_now.day
        hour = dt_now.hour
        minute = dt_now.minute
        second = dt_now.second

        # UTCにオフセットの加減算
        if offset_which == "plus":
            hour = hour + offset_hour
            minute = minute + offset_min
        elif offset_which == "minus":
            hour = hour - offset_hour
            minute = minute - offset_min
        else:
            output = None
            print("Error: :offset_which: value typo.")
            return(output)

        # うるう年の判定と設定
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    uruu = "y"
                else:
                    uruu = "n"
            else:
                uruu = "y"
        else:
            uruu = "n"
        
        if uruu == "y":
            month_size = [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        elif uruu == "n":
            month_size = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            output = None
            print(":urur: value typo.")
            return(output)          

        # 分の処理と時の加減算
        if minute > 59:
            hour = hour + 1
            minute = 0
        elif minute < 0:
            hour = hour - 1
            minute = 59

        # 時の処理と日の加減算
        if hour > 23:
            day = day + 1
            hour = hour - 24
        elif hour < 0:
            day = day - 1
            hour = hour + 24

        # 日の処理と月の加減算
        if day > month_size[month]:
            month = month + 1
            day = 1
        elif day < 1:
            month = month - 1
            if month == 0:
                day = month_size[12]
            elif month == 13:
                day = month_size[1]

        if month > 13:
            output = None
            print("Error: Incorrect month value.")
            return(output)
        elif month < 0:
            output = None
            print("Error: Incorrect month value.")
            return(output)

        # 月の処理と年の加減算
        if month == 13:
            year = year + 1
            month = 1
        elif month == 0:
            year = year - 1
            month = 12

        # 出力の処理
        if filter_nt == "year":
            output = year
        elif filter_nt == "month":
            output = month
        elif filter_nt == "day":
            output = day
        elif filter_nt == "hour":
            output = hour
        elif filter_nt == "minute":
            output = minute
        elif filter_nt == "second":
            output = second
        else:
            output = None
            print("Error: Incorrect filter value.")
            return(output)

        return(output)


    # 入力値確認
    if tz_set_nt == None:
        output = None
        print("Error: Incorrect timezone value.")
        return(output)
    elif filter_nt == None:
        output = None
        print("Error: Incorrect filter value.")
        return(output)
    else:
        pass

    # 入力値格納&変換
    tz_set_nt = str(tz_set_nt.upper())  # タイムゾーン設定
    filter_nt = str(filter_nt.lower())  # フィルター設定

    # フィルター値の正誤判定
    if filter_nt not in ["year", "month", "day", "hour", "minute", "second"]:
        output = None
        print("Error: Incorrect filter value.")
        return(output)

    # タイムゾーン(コード)処理
    if tz_set_nt == "GMT":
        offset_hour = 0
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "UTC":
        offset_hour = 0
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "ECT":
        offset_hour = 1
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "EET":
        offset_hour = 2
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "ART":
        offset_hour = 2
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "EAT":
        offset_hour = 3
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "MET":
        offset_hour = 3
        offset_min = 30
        offset_which = "plus"
    elif tz_set_nt == "NET":
        offset_hour = 4
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "PLT":
        offset_hour = 5
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "IST":
        offset_hour = 5
        offset_min = 30
        offset_which = "plus"
    elif tz_set_nt == "BST":
        offset_hour = 6
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "VST":
        offset_hour = 7
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "CTT":
        offset_hour = 8
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "JST":
        offset_hour = 9
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "ACT":
        offset_hour = 9
        offset_min = 30
        offset_which = "plus"
    elif tz_set_nt == "AET":
        offset_hour = 10
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "SST":
        offset_hour = 11
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "NST":
        offset_hour = 12
        offset_min = 0
        offset_which = "plus"
    elif tz_set_nt == "MIT":
        offset_hour = 11
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "HST":
        offset_hour = 10
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "AST":
        offset_hour = 9
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "PST":
        offset_hour = 8
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "PNT":
        offset_hour = 7
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "MST":
        offset_hour = 7
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "CST":
        offset_hour = 6
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "EST":
        offset_hour = 5
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "IET":
        offset_hour = 5
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "PRT":
        offset_hour = 4
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "CNT":
        offset_hour = 3
        offset_min = 30
        offset_which = "minus"
    elif tz_set_nt == "AGT":
        offset_hour = 3
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "BET":
        offset_hour = 3
        offset_min = 0
        offset_which = "minus"
    elif tz_set_nt == "CAT":
        offset_hour = 1
        offset_min = 0
        offset_which = "minus"
    else:
        output = None
        print("Error: Incorrect timezone value.")
        return(output)

    change()
    return(output)
