from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite qualquer origem

# Dicionário para armazenar as contas e seus saldos
accounts = {}


@app.route('/reset', methods=['POST'])
def reset():
    global accounts
    accounts = {}  # Reseta o dicionário de contas
    return jsonify(message="State reset successful"), 200


@app.route('/balance', methods=['GET'])
def get_balance():
    account_name = request.args.get(
        'account_name', "").strip()  # Mudei para 'account_name'
    print(f"Recebendo requisição para: {account_name}")  # Log para debug

    if not account_name:  # Se não foi informado o nome da conta
        return jsonify(error="Erro: Informe um nome de conta na URL. Exemplo: /balance?account_id=Paula"), 400

    balance = accounts.get(account_name)

    # Se a conta não existir
    if balance is None:
        # Conta não encontrada, retorna 404 com saldo 0
        return jsonify(balance=0), 404

    # Se a requisição aceitar JSON, retorna JSON
    if request.headers.get("Accept") == "application/json":
        return jsonify(balance=balance), 200

    # Caso contrário, retorna o HTML formatado
    return render_template("visual.html", account_name=account_name, balance=balance, accounts=accounts)


@app.route('/event', methods=['POST'])
def process_event():
    event = request.get_json()
    event_type = event.get('type')
    destination = event.get('destination')  # Agora pode ser um nome ou id
    origin = event.get('origin')  # Conta de origem para saque e transferência
    amount = event.get('amount', 0)

    # Processando evento de 'deposit'
    if event_type == 'deposit':
        if destination in accounts:
            accounts[destination] += amount
        else:
            accounts[destination] = amount
        return jsonify(destination={'id': destination, 'balance': accounts[destination]}), 201

    # Processando evento de 'withdraw'
    if event_type == 'withdraw':
        if origin not in accounts:
            return jsonify(error="Account not found"), 404
        if accounts[origin] < amount:
            return jsonify(error="Insufficient funds"), 400
        accounts[origin] -= amount
        return jsonify(origin={'id': origin, 'balance': accounts[origin]}), 201

    # Processando evento de 'transfer'
    if event_type == 'transfer':
        if origin not in accounts:
            return jsonify(error="Origin account not found"), 404
        if destination not in accounts:
            return jsonify(error="Destination account not found"), 404
        if accounts[origin] < amount:
            return jsonify(error="Insufficient funds"), 400
        accounts[origin] -= amount
        accounts[destination] += amount
        return jsonify(origin={'id': origin, 'balance': accounts[origin]}, destination={'id': destination, 'balance': accounts[destination]}), 201

    return jsonify(error='Invalid event type'), 400


if __name__ == '__main__':
    app.run(debug=True)
