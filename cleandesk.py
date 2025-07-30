from mover import organizar_pasta
from logger_setup import logger
import schedule
import time

def agendar_organizacao():
    schedule.every(30).minutes.do(organizar_pasta)
    logger.info("Agendamento iniciado: organização a cada 30 minutos.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    logger.info("Organização manual iniciada.")
    organizar_pasta()
    # Se quiser ativar o agendamento, descomente a linha abaixo:
    # agendar_organizacao()
