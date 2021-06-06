import schedule
import time

def job():
    print(f"Reading time")

# time
schedule.every(3).seconds.do(job)
iteration = 0

while True:
    schedule.run_pending()
    time.sleep(1)
