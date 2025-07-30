import zipfile
import os
from logger_setup import logger

def compactar_em_zip(pasta_origem, arquivo_zip):
    logger.info(f"Compactando {pasta_origem} em {arquivo_zip}")
    with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(pasta_origem):
            for file in files:
                caminho_completo = os.path.join(root, file)
                zipf.write(caminho_completo, os.path.relpath(caminho_completo, pasta_origem))
    logger.info("Compactação concluída.")
