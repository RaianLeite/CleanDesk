def identificar_categoria(arquivo_nome):
    extensoes = {
        'pdf': 'Documentos/PDFs',
        'jpg': 'Imagens',
        'png': 'Imagens',
        'exe': 'Executaveis',
        # adicione outras extensões e pastas aqui
    }

    ext = arquivo_nome.split('.')[-1].lower()
    return extensoes.get(ext, 'Outros')
