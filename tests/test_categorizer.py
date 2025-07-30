from categorizer import identificar_categoria

def test_identificar_categoria_pdf():
    assert identificar_categoria("arquivo.pdf") == "Documentos/PDFs"

def test_identificar_categoria_imagem():
    assert identificar_categoria("foto.jpg") == "Imagens"

def test_identificar_categoria_outros():
    assert identificar_categoria("arquivo.xyz") == "Outros"
