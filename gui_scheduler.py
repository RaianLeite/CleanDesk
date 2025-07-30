import tkinter as tk
import schedule
import threading
import time
from mover import organizar_pasta
from logger_setup import logger

def run_schedule(interval):
    if interval == "manual":
        logger.info("Organização manual iniciada via GUI.")
        organizar_pasta()
        return

    minutes = int(interval)
    logger.info(f"Agendamento iniciado via GUI: rodando a cada {minutes} minutos.")
    schedule.every(minutes).minutes.do(organizar_pasta)

    while True:
        schedule.run_pending()
        time.sleep(1)

def start_schedule():
    interval = schedule_var.get()
    t = threading.Thread(target=run_schedule, args=(interval,))
    t.daemon = True
    t.start()

# GUI
root = tk.Tk()
root.title("CleanDesk - Agendador")
root.geometry("320x500")

schedule_var = tk.StringVar(value="60")

# Curto prazo
tk.Label(root, text="Curto prazo", font=("Arial", 10, "bold")).pack(pady=5)
tk.Radiobutton(root, text="A cada 10 minutos", variable=schedule_var, value="10").pack(anchor="w")
tk.Radiobutton(root, text="A cada 30 minutos", variable=schedule_var, value="30").pack(anchor="w")
tk.Radiobutton(root, text="A cada 1 hora", variable=schedule_var, value="60").pack(anchor="w")

# Médio prazo
tk.Label(root, text="Médio prazo", font=("Arial", 10, "bold")).pack(pady=5)
tk.Radiobutton(root, text="A cada 3 horas", variable=schedule_var, value="180").pack(anchor="w")
tk.Radiobutton(root, text="A cada 6 horas", variable=schedule_var, value="360").pack(anchor="w")
tk.Radiobutton(root, text="A cada 12 horas", variable=schedule_var, value="720").pack(anchor="w")

# Longo prazo
tk.Label(root, text="Longo prazo", font=("Arial", 10, "bold")).pack(pady=5)
tk.Radiobutton(root, text="A cada 24 horas", variable=schedule_var, value="1440").pack(anchor="w")
tk.Radiobutton(root, text="A cada 3 dias", variable=schedule_var, value=str(3 * 1440)).pack(anchor="w")
tk.Radiobutton(root, text="A cada 7 dias", variable=schedule_var, value=str(7 * 1440)).pack(anchor="w")

# Execução manual
tk.Label(root, text="").pack()
tk.Radiobutton(root, text="Executar agora", variable=schedule_var, value="manual").pack(anchor="w")

# Botão iniciar
tk.Button(root, text="Iniciar", command=start_schedule).pack(pady=20)

root.mainloop()
