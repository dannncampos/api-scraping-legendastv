# Scraping Legendas TV

- Versão: 0.1
- Autor: Daniel Campos
- Data: 01/03/2021

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Crawlers desenvolvidos para a API

- **Legendas TV** => Busca de legendas por termo

## Disclaimer

O projeto tem como base a extração de dados do site legendas.tv com informações sobre quantidade de downloads de cada legenda disponível, nota dos usuários, autor ou responsável pelo envio e a respectiva data e hora.

### Consulta Legendas TV

A aplicação suporta login do usuário e pesquisa por termo ou título de filmes, seriados ou cartoons. 

#### Endpoints

**/legendastv/term** - Legendas TV API - **Argumentos****¹**:

- *term (str)*: The term to search.
- *user (str)*: Legendas Tv User's Login.
- *password (str)*: Legendas Tv User's Password.

    Retorno: 
- **JSON (dict)** - The JSON dict with the search details

**[¹]: Argumento obrigatório.**
**[²]: Argumento com default.**

# Camadas de desenvolvimento

- **Camada App**: EntryPoints de consulta
- **Camada Service**: Camada que contém tipos de captura, sessão de requisição, endpoints e variáveis globais
- **Camada Business**: Controle de ações do robô
- **Camada Broker**: Controle de requisições e negociação com o servidor alvo para captura de HTML e Download de documentos
- **Camada Parser**: Extração de dados do DOM, higienização dos dados e modelagem das informações para o formato JSON
- **Camada DAO**: Armazenamento e conexões de storage

### Ambientes

Em testes internos, com set de login e senha, criar arquivo **.env** com as informações de chaves para:

- DEFAULT_USER = '' # **Change it for Legendas Tv User Login**
- DEFAULT_PASSWORD = '' # **Change it for Legendas Tv User Password**
- ACCESS_KEY = '' # **Change it for Amazon AWS S3**
- SECRET_KEY = '' # **Change it for Amazon AWS S3**
- BUCKET = '' # **Change it for Amazon AWS S3**

### Buildando o docker

    docker build -t legendastvimg . && docker run -d --name legendastvcontainer -p 80:80 legendastvimg

### Executando Teste

Após fazer o build do Dockerfile e ter o container ativo, acesse o endereço em seu navegador: http://127.0.0.1/docs.

Clique em POST/legendastv/term -> Try it out -> Digite o termo de pesquisa (Ex. "Simpsons") e seu usuário e senha do site Legendas TV.

Clique em executar.

### Verificando os Testes Automatizados

$ pytest {arquivo}