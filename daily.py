# wonder日志  v0.5
import datetime

filename = "wonder_daily_log.txt"
date = datetime.date.today()
subject = input("今天想記錄哪一個領域？👽：")
entry = input("發生了什麽？🦊：")

with open(filename, "a", encoding="utf-8") as f:
    f.write(f"💊{date}|🪬{subject}|🪇{entry}  \n")

print("記錄成功！經驗值+1+1+1!🥰")
