import os
import shutil
from categorizer import identificar_categoria
from logger_setup import logger

def organizar_pasta(pasta_origem="C:/Users/raian/Downloads"):
    logger.info(f"Organizando a pasta: {pasta_origem}")
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            categoria = identificar_categoria(arquivo)
            pasta_destino = os.path.join(pasta_origem, categoria)

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            destino_final = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho_arquivo, destino_final)
            logger.info(f"Movido: {arquivo} -> {categoria}")
