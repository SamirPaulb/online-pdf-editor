import subprocess
import time
from datetime import date

schedule = [date(2012, 6, 3), date(2012, 6, 4), date(2012, 6, 5), date(2012, 6, 6),
            date(2012, 6, 10),
            date(2012, 6, 14), date(2012, 6, 15), date(2012, 6, 16), date(2012, 6, 17), date(2012, 6, 18),
            date(2012, 6, 19), date(2012, 6, 20),
            date(2012, 6, 29), date(2012, 7, 1), date(2012, 7, 2), date(2012, 7, 3), date(2012, 7, 4)]


def commit():
    process = subprocess.run('./commit.sh', shell=True, check=True, timeout=100)


print("Program started ...")
while len(schedule) > 0:
    for date in schedule:
        if date == date.today():
            for i in range(0, 3):
                file = open("./dummy.txt", "a")
                time.sleep(1)
                print("File opened")
                file.write("1\n")
                time.sleep(1)
                file.close()
                print("File Overwritten")
                time.sleep(2)
                print("Committed")
                commit()
                time.sleep(5)
            print("Committed on", date.today())
            schedule.remove(date)
    time.sleep(6)
