import schedule
import time
import subprocess

def run_backlink():
    subprocess.run(["python", "backlink_generator.py"])

def run_ctr():
    subprocess.run(["python", "ctr_simulator.py"])

def run_indexing():
    subprocess.run(["python", "indexing_booster.py"])

def run_content():
    subprocess.run(["python", "content_spawner.py"])

schedule.every(6).hours.do(run_backlink)
schedule.every(8).hours.do(run_ctr)
schedule.every().day.at("02:00").do(run_indexing)
schedule.every().day.at("04:00").do(run_content)

while True:
    schedule.run_pending()
    time.sleep(60)
