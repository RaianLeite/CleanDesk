import os
import shutil
import schedule
import time

# Mude aqui para a pasta que você quer organizar (ex: Downloads)
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# Dicionário com extensões e pastas correspondentes
EXTENSIONS_MAP = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Executáveis": [".exe", ".msi", ".bat"],
    "Arquivos Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Músicas": [".mp3", ".wav", ".flac"],
    # Pode adicionar mais categorias e extensões aqui
}

def organizar_pasta():
    print("Iniciando organização da pasta:", DOWNLOADS_FOLDER)
    arquivos = os.listdir(DOWNLOADS_FOLDER)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(DOWNLOADS_FOLDER, arquivo)

        # Ignorar pastas
        if os.path.isdir(caminho_arquivo):
            continue

        # Identificar extensão
        _, ext = os.path.splitext(arquivo)
        ext = ext.lower()

        # Procurar categoria da extensão
        destino_pasta = None
        for pasta, extensoes in EXTENSIONS_MAP.items():
            if ext in extensoes:
                destino_pasta = pasta
                break

        # Se não encontrou categoria, coloca em "Outros"
        if destino_pasta is None:
            destino_pasta = "Outros"

        pasta_destino = os.path.join(DOWNLOADS_FOLDER, destino_pasta)

        # Criar pasta destino se não existir
        if not os.path.exists(pasta_destino):
            os.mkdir(pasta_destino)

        # Mover arquivo para a pasta destino
        novo_caminho = os.path.join(pasta_destino, arquivo)
        print(f"Movendo {arquivo} para {pasta_destino}")
        shutil.move(caminho_arquivo, novo_caminho)

    print("Organização finalizada.")

def agendar_organizacao():
    # Agenda a organização para rodar a cada 30 minutos, por exemplo
    schedule.every(30).minutes.do(organizar_pasta)
    print("Agendamento iniciado: organização a cada 30 minutos.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Para rodar manualmente, basta chamar a função
    organizar_pasta()

    # Se quiser ativar o agendamento, descomente a linha abaixo:
    # agendar_organizacao()
