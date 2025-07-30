import schedule
import time
from mover import organizar_pasta

def job():
    print("Executando organização automática...")
    organizar_pasta()

def run_schedule():
    schedule.every(15).seconds.do(job)
    print("Agendamento iniciado: rodando a cada 1 hora.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
