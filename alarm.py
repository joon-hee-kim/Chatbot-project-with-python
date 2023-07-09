import datetime
import time

time.sleep(10)

import datetime

def get_current_time():
    now = datetime.datetime.now()
    print("현재 시간은 {}시 {}분입니다.".format(now.hour, now.minute))
    print("오늘은 {}년 {}월 {}일입니다.".format(now.year, now.month, now.day))
get_current_time()  

def set_medication_reminder():
    while True:
        user_input = input("약 복용 알림 시간대를 설정해주세요. (HH:MM) ")
        try:
            hour, minute = map(int, user_input.split(':'))
            alarm_time = datetime.time(hour=hour, minute=minute)
            break
        except ValueError:
            print("입력이 잘못되었습니다. 다시 입력해주세요.")
            continue

    while True:
        now = datetime.datetime.now().time()
        if now >= alarm_time:
            print("약 복용 시간입니다.")
            break
        time.sleep(30)  

set_medication_reminder()
