import schedule
import time
from notifier.skin_checker.py import check_skin_availability
from notifier.email_notifier import send_email
from config.config import RECIPIENT_EMAIL

def job():
    skin_name = 'Chupinazo'
    if check_skin_availability(skin_name):
        send_email('Skin Available', f'The skin {skin_name} is now available.', RECIPIENT_EMAIL)

schedule.every(20).seconds.do(job)

def run():
    while True:
        schedule.run_pending()
        time.sleep(1)