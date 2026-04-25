import csv
from datetime import date
import pywhatkit
import time

today = date.today()
today_month = today.month
today_day = today.day


with open("birthdays.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row["Name"]
        phone = row["Phone"]
        month = int(row["month"])
        day = int(row["day"])
        if today_month == month and today_day == day:
            print(f"{name} 🎉 Birthday Today!")

            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone,
                message=f"🎂 Happy Birthday {name}! Have a great day!",
                wait_time=15,
                tab_close=True
            )

            time.sleep(5)
        else:
            print(f"{name} → Not today")

print("Program ended")
