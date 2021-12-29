import os
import crossula
from flask import Flask, jsonify, request

app = Flask(__name__)

get_crossula = crossula.Client(
        authKey=os.getenv("authKey"),
        clientId=os.getenv("clientId")
)


@app.route("/")
def index():
    return jsonify({200: "Okay"})


@app.route("/createAccount")
def create_account():
    get_name = request.args.get("name")

    try:
        res = get_crossula.create_account({"name": get_name})
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/getAccountList")
def get_account_list():
    try:
        res = get_crossula.get_account_list()
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/createIBAN")
def create_iban():
    get_account_id = request.args.get("accountId")

    try:
        res = get_crossula.create_account_iban(get_account_id)
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/getAllIBANS")
def get_all_ibans():
    get_account_id = request.args.get("accountId")

    try:
        res = get_crossula.get_account_ibans(get_account_id)
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/getIBANBalances")
def get_iban_balances():
    try:
        res = get_crossula.get_account_balances()
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/getIBANBalanace")
def get_iban_balance():
    get_account_id = request.args.get("accountId")
    get_account_iban = request.args.get("iban")

    try:
        res = get_crossula.get_account_iban_balances(get_account_id, get_account_iban)
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/getTransactionList")
def get_transaction_list():
    get_filter = request.args.get("filter")

    try:
        res = get_crossula.get_transaction_list(get_filter)
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/makeInternalTransfer")
def make_internal_transfer():
    get_params = request.args.get("params")

    try:
        res = get_crossula.make_internal_transfer(12345, get_params)
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/makeSepaTransfer")
def make_sepa_transfer():
    get_params = request.args.get("params")

    try:
        res = get_crossula.make_sepa_transfer(12345, get_params)
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


@app.route("/getTransactionById")
def get_transaction_by_id():
    get_transaction_id = request.args.get("transaction_id")

    try:
        res = get_crossula.get_transaction_by_id(get_transaction_id)
        return jsonify({200: res})

    except Exception as e:
        return jsonify({500: str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=20002, debug=True)