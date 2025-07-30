import logging
import os
import sys
from pathlib import Path
from datetime import datetime

def _limpar_logs_antigos(log_dir: Path):
    arquivos = sorted(
        [f for f in log_dir.glob("*.txt") if f.is_file()],
        key=lambda f: f.name
    )
    if len(arquivos) > 3:
        arquivos_para_excluir = arquivos[:len(arquivos) - 3]
        for arquivo in arquivos_para_excluir:
            try:
                arquivo.unlink()
            except Exception as e:
                print(f"Erro ao deletar log antigo: {arquivo.name} - {e}")

def setup_logger():
    if hasattr(sys, '_MEIPASS'):
        base_dir = Path(sys.executable).parent
    else:
        base_dir = Path(__file__).parent

    log_dir = base_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    current_month = datetime.now().strftime("%Y-%m")
    log_path = log_dir / f"{current_month}.txt"

    _limpar_logs_antigos(log_dir)

    logger = logging.getLogger("CleanDesk")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()
