import json
from .exceptions import CrossulaException
import requests

class Client:
    def __init__(self, authKey="", clientId=""):
        self.authKey = authKey
        self.clientId = clientId
        self.api_url = "https://client.demo.crassu.la"
        self.headers = {
            "Authorization": self.authKey
        }

    def __send_request(self, request_url, method="GET", data={}, headers=None):
        if headers is None:
            headers = self.headers
        
        if method == "GET":
            r = requests.get(f"{self.api_url}/{request_url}", headers=headers, params=data)
        
        else:
            headers["Content-Type"] = "application/json"

            if type(data) != dict:
                    data = json.loads(data)
            
            if method == "POST":
                r = requests.post(f"{self.api_url}/{request_url}", headers=headers, data=json.dumps(data))

            elif method == "PUT":
                r = requests.put(f"{self.api_url}/{request_url}", headers=headers, data=json.dumps(data))
            
        if r.status_code != 200:
            raise CrossulaException(f"{r.status_code}")

        return json.loads(r.text)


    """ Create an account (Subaccount) """
    def create_account(self, params):
        return self.__send_request(f"api/clients/{self.clientId}/accounts", method="POST", data=params)

    """ Close account (Subaccount) """
    def close_account(self, accountId, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/close", method="PUT", data=params)

    """ Get account (Subaccount) information """
    def get_account_info(self, accountId, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}", data=params)

    """ Create account (Subaccount) IBAN """
    def create_account_iban(self, accountId, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/iban", method="POST", data=params)
    
    """ Get account (Subaccount) IBAN list """
    def get_account_ibans(self, accountId, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/iban", data=params)

    def get_account_balances(self, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/balances", data=params)

    """ Get account (Subaccount) IBAN balances """
    def get_account_iban_balances(self, accountId, accountIBAN, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/iban/{accountIBAN}/balances", data=params)

    """ Get transactions by transactionID """
    def get_transaction_by_id(self, transactionId, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/transactions/{transactionId}", data=params)

    """ Currency exchange """
    def account_exchange(self, params):
        return self.__send_request(f"api/clients/{self.clientId}/currency/exchange", method="POST", data=params)

    """ Make internal transfer """
    def make_internal_transfer(self, XConfirmationCode, params):
        headers = self.headers.copy()
        headers["X-Confirmation-Code"] = str(XConfirmationCode)

        return self.__send_request(f"api/clients/{self.clientId}/transfer/internal", method="POST", data=params, headers=headers)

    """ Make sepa transfer """
    def make_sepa_transfer(self, XConfirmationCode, params):
        headers = self.headers.copy()
        headers["X-Confirmation-Code"] = str(XConfirmationCode)

        return self.__send_request(f"api/clients/{self.clientId}/transfer/sepa", method="POST", data=params, headers=headers)

    """ Make swift transfer """    
    def make_swift_transfer(self, XConfirmationCode, params):
        headers = self.headers.copy()
        headers["X-Confirmation-Code"] = str(XConfirmationCode)

        return self.__send_request(f"api/clients/{self.clientId}/transfer/swift", method="POST", data=params, headers=headers)

    """ Get transaction list """
    def get_transaction_list(self, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/transactions", data=params)

    """ Get account (Subaccount) list """
    def get_account_list(self, params={}):
        return self.__send_request(f"api/clients/{self.clientId}/accounts", data=params)