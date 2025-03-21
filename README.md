
ebanx_challenge
Este projeto é uma solução simples de API para gerenciar contas bancárias utilizando Flask, permitindo que os usuários criem contas, depositem, sacem e transfiram valores. Além disso, ele também oferece uma visualização de saldo e uma funcionalidade de reset para reiniciar os dados das contas.

Funcionalidades
Criar conta com depósito inicial: Através de um POST no endpoint /event com tipo "deposit", você pode criar uma conta com um saldo inicial.
Consultar saldo de uma conta: Um GET para o endpoint /balance retorna o saldo da conta fornecida.
Depósito em uma conta existente: Através de um POST no endpoint /event com tipo "deposit", você pode adicionar saldo a uma conta existente.
Saque de uma conta existente: Um POST no endpoint /event com tipo "withdraw" permite retirar um valor de uma conta existente.
Transferência entre contas: Um POST no endpoint /event com tipo "transfer" permite transferir valores entre duas contas existentes.
Resetar estado das contas: Um POST no endpoint /reset limpa todas as contas e seus saldos.
Estrutura do Projeto
index.py: Arquivo principal da aplicação, responsável pela configuração da API e gerenciamento das contas.
templates/visual.html: Template HTML para exibição de saldo da conta e lista de outras contas.
README.md: Este arquivo de documentação.
.gitignore: Arquivo para evitar o versionamento de arquivos desnecessários, como o ambiente virtual.


Como Rodar a Aplicação
Pré-requisitos
Python 3.x
Pip (gerenciador de pacotes do Python)
Passos para rodar localmente

Clone este repositório:
git clone https://github.com/codebypaula/ebanx_challenge.git

Instale as dependências:
Crie um ambiente virtual e instale as dependências.
cd ebanx_challenge
python3 -m venv .venv
source .venv/bin/activate , use .venv\Scripts\activate
pip install -r requirements.txt
 
Inicie a aplicação:
Para iniciar o servidor, execute:
python index.py

A aplicação estará rodando em http://127.0.0.1:5000.

Testando a API
Você pode testar a aplicação utilizando ferramentas como Postman ou curl. Aqui estão alguns exemplos de como interagir com os endpoints:

Criar uma conta com depósito inicial:
curl -X POST http://127.0.0.1:5000/event -H "Content-Type: application/json" -d '{"type": "deposit", "destination": "João", "amount": 100}'

Consultar saldo de uma conta:
curl http://127.0.0.1:5000/balance?account_name=João

Sacar de uma conta:
curl -X POST http://127.0.0.1:5000/event -H "Content-Type: application/json" -d '{"type": "withdraw", "origin": "João", "amount": 50}'

Transferir entre contas:
curl -X POST http://127.0.0.1:5000/event -H "Content-Type: application/json" -d '{"type": "transfer", "origin": "João", "destination": "Paula", "amount": 30}'

Resetar o estado da aplicação:
curl -X POST http://127.0.0.1:5000/reset
