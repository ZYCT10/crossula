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
            r = requests.get(f"{self.api_url}/{request_url}", headers=headers)
        elif method == "POST":
            r = requests.post(f"{self.api_url}/{request_url}", headers=headers, data=data)
        elif method == "PUT":
            r = requests.put(f"{self.api_url}/{request_url}", headers=headers, data=data)
        
        if r.status_code != 200:
            raise CrossulaException(f"{r.status_code}")
            
        return r.text
    
    def create_account(self, param):
        return self.__send_request(f"api/clients/{self.clientId}/accounts", method="POST", data=param)

    def close_account(self, accountId):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/close", method="PUT")

    def get_account_info(self, accountId):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}")

    def create_account_iban(self, accountId):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/iban", method="POST")
    
    def get_account_ibans(self, accountId):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/iban")

    def get_account_iban_info(self, accountId, accountIBAN):
        return self.__send_request(f"api/clients/{self.clientId}/accounts/{accountId}/iban/{accountIBAN}/balances")

    def account_exchange(self, body):
        return self.__send_request(f"api/clients/{self.clientId}/currency/exchange", method="POST", data=json.dumps(body))

    def make_sepa_transfer(self, XConfirmationCode, body):
        headers = self.headers.copy()
        headers["X-Confirmation-Code"] = XConfirmationCode

        return self.__send_request(f"api/clients/{self.clientId}/transfer/sepa", method="POST", data=json.dumps(body), headers=headers)
    
    def make_swift_transfer(self, XConfirmationCode, body):
        headers = self.headers.copy()
        headers["X-Confirmation-Code"] = XConfirmationCode

        return self.__send_request(f"api/clients/{self.clientId}/transfer/swift", method="POST", data=json.dumps(body), headers=headers)

    def get_transaction_list(self):
        return self.__send_request(f"api/clients/{self.clientId}/transactions")

    def get_account_list(self):
        return self.__send_request(f"api/clients/{self.clientId}/accounts")