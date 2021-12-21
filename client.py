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
    
    def __send_request(self, request_url, method="GET", data={}):
        if method == "GET":
            r = requests.get(f"{self.api_url}/{request_url}", headers=self.headers)

        elif method == "POST":
            r = requests.get(f"{self.api_url}/{request_url}", headers=self.headers, data=data)
        
        elif method == "PUT":
            r = requests.put(f"{self.api_url}/{request_url}", headers=self.headers, data=json.dumps(data))

        if r.status_code != 200:
            raise CrossulaException(f"CrossulaException: {r.text}")
            
        return r.text
    
    def get_account_list(self):
        return self.__send_request(f"api/clients/{self.clientId}/accounts")