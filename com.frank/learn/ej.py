# -*- coding: utf-8 -*-
import schedule
import time
print("Hello World")

def job():
    print("job doing ...")
    with open(file="E:/t1.txt", mode="r+", encoding="utf-8") as f:
        ftextlist = f.readlines()
        print("content=",ftextlist)
        t= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        f.write("job doing"+t+"\n")
    print("job finish")

print("start running...")

schedule.every(5).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

