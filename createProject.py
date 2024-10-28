from locust import HttpUser, task, between
from access_token import AccessToken
from time import sleep

class User(HttpUser):
    wait_time = between(1, 2)
    token_manager = AccessToken()
    host = 'https://dev-apiv1.1000saudara.com'

    def on_start(self):
        self.token_manager.fetch_token()

    @task
    def login(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token_manager.token}'
        }
        data = {
            "Origins": {
                "Source": "mss_app_quotation",
                "Version": "1"
            },
            "Token": "",
            "UserCode": "RTFQItGmA9g=",
            "Value": {
                "Name": "AA Group",
                "Address": "Jl.Coor",
                "KecamatanId": "OM/pT5XLjY4\u003d",
                "KabKotaId": "rvIXqJf50yI\u003d",
                "ProvinsiId": "3Aib7klhsSs\u003d",
                "CoorLa": "0",
                "CoorLo": "0",
                "EstimateStartDate": "2024-08-29T00:00:00",
                "EstimateEndDate": "null",
                "MaxBudget": 1232,
                "PICAdmin": "kTrPW/goank=",
                "PICManagerProject": "tMq4MXaRqTQ=",
                "PICFinance": "CUam0J1lJ3o="  
            }
        }

        response = self.client.post('/apiproyek/wb/Project/CreateProject', json=data, headers=headers)
        if response.status_code == 200:
            print("Login successful!")
        else:
            print(f'Login failed: {response.text}')

    # @task
    # def access(self):
    #     if self.token_manager.token:
    #         headers = {
    #             'X-MSSAPI-KEY': 'DPEqC6x0Rh8eU5QhtjS1'
    #         }
    #         response = self.client.post('/auth/access', headers=headers, data='')
    #     else:
    #         print('Token is not available.')
