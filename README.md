# Smart Wallet API

A Smart Wallet API é uma API RESTful desenvolvida com Django e Django REST Framework, voltada para a gestão de investimentos. Ela oferece endpoints seguros para criar, ler, atualizar e excluir registros de investimentos, e inclui autenticação via JWT, validações customizadas e documentação interativa.

# Endpoints Principais
## Investimentos:
/api/investments/ – Permite criar, listar, atualizar e excluir registros de investimentos.

## Autenticação:
/api/token/ – Obtenção dos tokens de acesso e refresh.

/api/token/refresh/ – Renovação do token de acesso.

## A documentação interativa pode ser acessada através das seguintes URLs:

Swagger UI: /swagger/
ReDoc: /redoc/
Estas interfaces permitem testar os endpoints e visualizar os esquemas de entrada e saída da API.

Wiki
Para detalhes mais aprofundados sobre o projeto, arquitetura, decisões de design, exemplos de uso e instruções de deploy, consulte a Wiki do Projeto.

## Para configurar o projeto localmente, siga os passos abaixo:

Clone o repositório:
```bash
git clone https://github.com/BernardoGatt0/SmartWalletInvest.git
cd SmartWalletInvest
```
Crie e ative um ambiente virtual:
```Python
python -m venv venv
source venv/bin/activate  # No Windows utilize: venv\Scripts\activate
```
Instale as dependências:
```Python
pip install -r requirements.txt
```
Aplique as migrações do banco de dados:
```Python
python manage.py migrate
```
Inicie o servidor de desenvolvimento:
```Python
python manage.py runserver
```