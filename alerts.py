import schedule
import time
from scraper import get_jobs

def job_alert():

    jobs = get_jobs()

    print("Nuevos empleos encontrados:")

    for job in jobs:
        print(job)

schedule.every(6).hours.do(job_alert)

def start_alerts():

    while True:
        schedule.run_pending()
        time.sleep(60)