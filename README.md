# Como Criar o Ambiente Virtual com Python

Este tutorial explica como criar e configurar um ambiente virtual utilizando o Python para o seu projeto. O uso de ambientes virtuais é altamente recomendado para gerenciar dependências de forma isolada, evitando conflitos entre pacotes e garantindo que o projeto tenha as versões corretas das bibliotecas.

### Pré-requisitos

- **Python 3.3 ou superior** (Python 3.10 recomendado)
- **pip** (gerenciador de pacotes do Python, que já deve vir instalado com o Python)

### Passo 1: Instalar o Python (se necessário)

Caso o Python não esteja instalado, você pode fazer o download da versão mais recente no [site oficial do Python](https://www.python.org/downloads/). Siga as instruções para o seu sistema operacional.

### Passo 2: Obtenha o código

```bash
https://github.com/leocassiosilva/mini-twitter.git
```


### Passo 3: Criar o Ambiente Virtual

1. Navegue até o diretório onde deseja criar o ambiente virtual.
2. Execute o comando abaixo para criar o ambiente virtual:

   **Linux ou macOS:**
     ```bash
     python3 -m venv nome_do_ambiente
     ```
   **Windows:**
    ```bash
    python -m venv nome_do_ambiente
    ```
    Após a criação, você provavelmente já estará no ambiente virtual.

### Passo 4: Ativar o Ambiente Virtual
1. Execute o comando abaixo para ativar o ambiente virtual:

   **Linux ou macOS:**
     ```bash
     source nome_do_ambiente/bin/activate
     ```
   **Windows:**
    ```bash
    .\nome_do_ambiente\Scripts\activate
    ```
### Passo 5: Instalar as Dependências
1. Execute o comando abaixo para ativar o ambiente virtual:
     ```bash
     pip install -r requirements.txt
     ```
### Passo 6: Criar o Banco de Dados
No seu projeto Django, a configuração do banco de dados já está pronta no arquivo settings.py, e você só precisa criar o arquivo .env com as variáveis de ambiente necessárias. Esse arquivo deve conter as informações de configuração do banco de dados e outras configurações sensíveis.

```bash
  SECRET_KEY=your_secret_key
  DEBUG=True
  PASSWORD_POSTGRES='sua_senha'
  USER_POSTGRES='seu_user'
  DATABASE_POSTGRES='seu_banco'
  HOST_POSTGRES='localhost'
  PORT_POSTGRES='5432'
  DEV=False
```

### Passo 6: Executar as Migrações
```bash
  python manage.py migrate
```
### Passo 6: Executar o Projeto
Agora você pode rodar o servidor de desenvolvimento do Django:
```bash
  python manage.py runserver
```
Neste momento seu banco estará sem nenhhum usuário cadastrado. O sistema conta com cadastro pela interface, mas, caso queira, é possível criar um usuário pela linha de comando. Basta executar este comando e informar o que for pedido:
```bash
python manage.py createuser
```
