# Smart Wallet API

A **Smart Wallet API** é uma API RESTful desenvolvida com **Django** e **Django REST Framework**, focada na gestão de investimentos. Ela oferece endpoints seguros para criar, ler, atualizar e excluir registros de investimentos, além de autenticação via **JWT**, validações personalizadas e documentação interativa.

---

## Endpoints Principais

### Investimentos
- **`GET /api/investments/`** – Lista todos os investimentos.
- **`POST /api/investments/`** – Cria um novo investimento.
- **`GET /api/investments/{id}/`** – Retorna detalhes de um investimento específico.
- **`PUT /api/investments/{id}/`** – Atualiza completamente um investimento.
- **`PATCH /api/investments/{id}/`** – Atualiza parcialmente um investimento.
- **`DELETE /api/investments/{id}/`** – Exclui um investimento.

### Tipos de investimentos
- **`GET /api/investment-types/`** – Lista todos os tipos de investimentos.
- **`POST /api/investment-types/`** – Cria um novo tipo de investimento.
- **`GET /api/investment-types/{id}/`** – Retorna detalhes de um tipo de investimento específico.
- **`PUT /api/investment-types/{id}/`** – Atualiza completamente um tipo de investimento.
- **`PATCH /api/investment-types/{id}/`** – Atualiza parcialmente um tipo de investimento.
- **`DELETE /api/investment-types/{id}/`** – Exclui um tipo de investimento.

### Dividendos
- **`GET /api/dividends/`** – Lista todos os dividendos.
- **`POST /api/dividends/`** – Cria um novo dividendo.
- **`GET /api/dividends/{id}/`** – Retorna detalhes de um dividendo específico.
- **`PUT /api/dividends/{id}/`** – Atualiza completamente um dividendo.
- **`PATCH /api/dividends/{id}/`** – Atualiza parcialmente um dividendo.
- **`DELETE /api/dividends/{id}/`** – Exclui um dividendo.

### Carteira
- **`GET /api/wallets/dividends/{id}/user/`** – Retorna a soma dos dividentos de um usuário.
- **`GET /api/wallets/investments/{id}/user/`** – Retorna a soma dos investimentos de um usuário.

### Autenticação
- **`POST /api/token/`** – Obtém tokens de acesso e refresh.
- **`POST /api/token/refresh/`** – Renova o token de acesso.

## A documentação interativa pode ser acessada através das seguintes URLs:

Swagger UI: /swagger/
ReDoc: /redoc/
Estas interfaces permitem testar os endpoints e visualizar os esquemas de entrada e saída da API.

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
## Testes

Utilizamos pytest para realizar os testes automatizados. Para executar os testes, basta rodar:
```Python
pytest
```
Os testes serão executados em um ambiente isolado (banco de dados de teste), garantindo que suas migrações e funcionalidades estejam corretas.