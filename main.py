
from flows.flow1 import Flow1
from flows.flow2 import Flow2
from apscheduler.schedulers.blocking import BlockingScheduler
import threading
from apscheduler.triggers.cron import CronTrigger
import logging
import json

# Logger pour voir les exécutions dans le terminal
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Création d’un verrou global pour ne pas utiliser le fichier en même temps
file_lock = threading.Lock()

with open("env_var.json", "r") as f:
    env_var = json.load(f)

client_code = env_var['client_code']

def run_flow1():
    with file_lock:
        flow = Flow1(name="flow1", client_code=client_code, output_folder_path="./output_folder", output_file="flows.csv")
        flow.apply()
        logging.info("flow1 exécuté")


def run_flow2():
    with file_lock:
        flow = Flow2(name="flow2", client_code=client_code, output_folder_path="./output_folder", output_file="flows.csv")
        flow.apply()
        logging.info("flow2 exécuté")


if __name__ == "__main__":

    cron_flow1 = next(job["cron"] for job in env_var["scripts"] if job["name"] == "script1")
    flow1_trigger = CronTrigger.from_crontab(cron_flow1)
    cron_flow2 = next(job["cron"] for job in env_var["scripts"] if job["name"] == "script2")
    flow2_trigger = CronTrigger.from_crontab(cron_flow2)

    scheduler = BlockingScheduler()
    scheduler.add_job(run_flow1, trigger=flow1_trigger)
    scheduler.add_job(run_flow2, trigger=flow2_trigger)

    scheduler.start()
