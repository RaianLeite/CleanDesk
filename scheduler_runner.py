import schedule
import time
from mover import organizar_pasta
from logger_setup import logger

def job():
    logger.info("Executando organização automática...")
    organizar_pasta()

def run_schedule():
    schedule.every(15).seconds.do(job)
    logger.info("Agendamento iniciado: rodando a cada 15 segundos.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
