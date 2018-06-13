# -*- coding: utf-8 -*-
import schedule
import time
print("Hello World")

def job():
    print("job doing ...")

name = 'zhangsan'
print(job())

schedule.every(5).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
