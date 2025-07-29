# 🧹 CleanDesk

O **CleanDesk** é um organizador automático de arquivos da pasta **Downloads**, desenvolvido em **Python**. Ele facilita a organização do seu computador movendo arquivos para pastas específicas com base em sua extensão, de forma simples e automatizada.

---

## 📸 Demonstração *(opcional)*

> *(Reservado para colocar um GIF ou print do programa funcionando)*

---

## 🚀 Funcionalidades

- Organização automática por tipo de arquivo (PDF, imagens, executáveis, etc.)
- Execução manual ou modo automático com agendamento (\`schedule\`)
- Geração de executável \`.exe\` para facilitar o uso no Windows
- Ícone personalizado no executável
- Código modular e de fácil manutenção

---

## 🧰 Tecnologias e Bibliotecas

- **Python 3.x**
- \`os\` – manipulação de diretórios  
- \`shutil\` – operações de cópia e movimentação de arquivos  
- \`schedule\` – agendamento de execução automática  
- \`pyinstaller\` – empacotamento para \`.exe\`

---

## 📥 Instalação

1. **Clone o repositório:**

```
git clone https://github.com/seu-usuario/CleanDesk.git
cd CleanDesk
```

2. **(Opcional) Crie e ative um ambiente virtual:**

```
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\\Scripts\\activate       # Windows
```

3. **Instale as dependências:**

```
pip install schedule
```

---

## ▶️ Como Executar

### Execução Manual

```
python main.py
```

### Execução com Agendamento

```
python schedule.py
```

---

## 💻 Como Gerar um Executável \`.exe\`

1. Instale o PyInstaller:

```
pip install pyinstaller
```

2. Gere o executável com ícone personalizado:

```
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

> O executável será criado na pasta \`dist/\`.

---

## 📂 Estrutura do Projeto

```
📁 CleanDesk
├── main.py           # Script principal
├── schedule.py       # Script com agendamento
├── icon.ico          # Ícone para o executável
├── README.md         # Documentação
├── .gitignore
└── dist/             # Executável gerado
```

---

## 🔮 Funcionalidades Futuras

- Interface gráfica com \`tkinter\` ou \`PyQt\`
- Definição de regras personalizadas pelo usuário
- Integração com notificações da área de trabalho
- Suporte a múltiplas pastas monitoradas

---

## ❗ Observações

- O script foi desenvolvido para a pasta **Downloads** do usuário. Verifique se os caminhos estão corretos no seu sistema.
- É necessário que o Python esteja instalado para executar diretamente os scripts \`.py\`.

---

## 👨‍💻 Autor

**Raian Dal Piero Leite**  
📧 [raianleite97@gmail.com](mailto:raianleite97@gmail.com)  
📍 Belo Horizonte – MG

---

> Projeto pessoal criado como prática de automação e organização de arquivos com Python.
