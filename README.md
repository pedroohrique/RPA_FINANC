# Sistema de Automação Financeira

Este projeto é um sistema de automação que coleta dados financeiros através do WhatsApp Web, processa essas informações e as armazena em um banco de dados SQL Server.

## Funcionalidades

- Coleta automática de mensagens do grupo financeiro no WhatsApp
- Processamento e validação dos dados coletados
- Armazenamento em banco de dados SQL Server
- Sistema de logging para acompanhamento das operações

## Pré-requisitos

- Python 3.x
- SQL Server
- Chrome Browser
- ChromeDriver
- pyodbc
- selenium

## Configuração do Ambiente

### 1. Instalação do Python e Dependências

```bash
# Instalar as dependências do projeto
pip install pyodbc selenium
```

### 2. Configuração do Banco de Dados

1. Certifique-se de ter o SQL Server instalado e rodando
2. Crie um banco de dados chamado 'FINANCEIRO'
3. Configure as credenciais de acesso no arquivo `database/connection.py`

### 3. Configuração do Chrome e ChromeDriver

1. Instale o Chrome Browser
2. Baixe o ChromeDriver compatível com sua versão do Chrome
3. Configure as variáveis de ambiente:
   - `CHROMEDRIVER_PATH`: Caminho para o executável do ChromeDriver
   - `CHROME_PATH`: Caminho para o executável do Chrome

### 4. Configuração do WhatsApp Web

1. O sistema utiliza um perfil específico do Chrome para manter a sessão do WhatsApp Web
2. Configure o caminho do perfil no arquivo `utils/browser.py`:
   ```python
   options.add_argument(r"user-data-dir=C:\\whatappcache")
   ```

## Estrutura do Projeto

```
app/
├── database/
│   ├── connection.py    # Configuração da conexão com o banco
│   └── querys.py        # Queries SQL
├── services/
│   ├── coleta.py        # Classe principal de automação
│   ├── data_handler.py  # Processamento dos dados
│   └── scrap.py         # Web scraping do WhatsApp
└── utils/
    ├── browser.py       # Configuração do navegador
    └── logger.py        # Sistema de logging
```

## Como Usar

1. Certifique-se de que todas as configurações estão corretas
2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

3. O sistema irá:
   - Abrir o WhatsApp Web
   - Coletar as mensagens do grupo financeiro
   - Processar os dados
   - Armazenar no banco de dados

## Formato das Mensagens

As mensagens no grupo financeiro devem seguir o seguinte formato:
```
ID
Data da Compra
Valor
Descrição
Local
Forma de Pagamento
Parcelamento
Quantidade de Parcelas
Categoria
```

## Logs

Os logs do sistema são armazenados em `utils/log_aplicacao.txt` e incluem:
- Data e hora da operação
- Nível do log
- Nome do módulo
- Função executada
- Mensagem
- Número da linha

## Observações Importantes

- Mantenha o Chrome e o ChromeDriver atualizados
- Certifique-se de que o WhatsApp Web está logado antes de executar o sistema
- O sistema utiliza um perfil específico do Chrome para manter a sessão
- Verifique os logs em caso de erros ou problemas 