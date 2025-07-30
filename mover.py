import os
import shutil
from categorizer import identificar_categoria
from logger_setup import logger

def organizar_pasta(pasta_origem="C:/Users/raian/Downloads"):
    logger.info(f"Organizando a pasta: {pasta_origem}")

    pasta_outros = os.path.join(pasta_origem, "Outros")
    if not os.path.exists(pasta_outros):
        os.makedirs(pasta_outros)

    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            categoria = identificar_categoria(arquivo)

            if not categoria:
                categoria = "Outros"

            pasta_destino = os.path.join(pasta_origem, categoria)
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            destino_final = os.path.join(pasta_destino, arquivo)

            if os.path.exists(destino_final):
                logger.warning(f"Arquivo já existe no destino e será sobrescrito: {destino_final}")
                os.remove(destino_final)

            shutil.move(caminho_arquivo, destino_final)
            logger.info(f"Movido: {arquivo} -> {categoria}")
