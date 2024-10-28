# from flask  import Flask, request
# from random import randint
# from time import sleep

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "OK"

# @app.route("/about")
# def about():
#     return "OK"

# @app.route("/random")
# def rndm():
#     sleep(randint(0,2))
#     return "OK"

# @app.route("/item")
# def items():
#     item_id = request.args.get("id", None)
#     return f"OK - {item_id}"

# @app.route("/login", methods=["GET","POST"])
# def login():
#     if request.method == "POST":
#         return "OK_POST"
#     else:
#         return "OK_GET"

# if __name__ == "__main__":
#     app.run()



from locust import HttpUser, task, between
from access_token import AccessToken 
from login  import  LoginTask
from time import sleep
import random
import string

def generate_random_name(length=6):
    # Membuat nama acak dengan huruf dan angka
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return "AA" + random_part  # Menambahkan "AA" di depan


class User(HttpUser):
    wait_time = between(1, 2)
    host = 'https://dev-apiv1.1000saudara.com'
    token_manager = AccessToken() 

    def on_start(self):
        # Panggil method untuk mengambil token saat pengguna mulai
        self.token_manager.fetch_token()

    @task
    def login(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token_manager.token}'
        }
        data = {
            "Token": "",
            "UserCode": "",
            "Origins": {
                "Source": "app_mitra",
                "Version": ""
            },
            "Value": {
                "Username": "088210068283",
                "Password": "12345"
            }
        }

        response = self.client.post('/apiproyek/wb/User/login', json=data, headers=headers)
        if response.status_code == 200:
            print("Login successful!")
        else:
            print(f'Login failed: {response.text}')

    @task
    def access(self):
        if self.token_manager.token:
            headers = {
                'X-MSSAPI-KEY': 'DPEqC6x0Rh8eU5QhtjS1'
            }
            response = self.client.post('/auth/access', headers=headers, data='')
        else:
            print('Token is not available.')

 # ini Untuk Buat Project
    # @task
    # def createProject(self):
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {self.token_manager.token}'
    #     }
    #     data = {
    #         "Origins": {
    #             "Source": "mss_app_quotation",
    #             "Version": "1"
    #         },
    #         "Token": "",
    #         "UserCode": "RTFQItGmA9g=",
    #         "Value": {
    #             "Name": generate_random_name(),
    #             "Address": "Jl.Coor",
    #             "KecamatanId": "OM/pT5XLjY4\u003d",
    #             "KabKotaId": "rvIXqJf50yI\u003d",
    #             "ProvinsiId": "3Aib7klhsSs\u003d",
    #             "CoorLa": "0",
    #             "CoorLo": "0",
    #             "EstimateStartDate": "2024-08-29T00:00:00",
    #             "EstimateEndDate": None,
    #             "MaxBudget": 1232,
    #             "PICAdmin": "kTrPW/goank=",
    #             "PICManagerProject": "tMq4MXaRqTQ=",
    #             "PICFinance": "CUam0J1lJ3o="  
    #         }
    #     }

    #     response = self.client.post('/apiproyek/wb/Project/CreateProject', json=data, headers=headers)
    #     if response.status_code == 200:
    #         json_response = response.json()
    #         print(f"Full Response: {json_response}") 
    #         msg = json_response.get('value', {}).get('response')
    #         print(f"Message: {msg}")
    #     else:
    #         print(f'Create failed: {response.text}')
   
    @task
    def createProject(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token_manager.token}'
        }
        data = {
            "Token": "",
            "UserCode": "RTFQItGmA9g=",
            "Origins": {
                "Source": "app_mitra",
                "Version": ""
            },
            "Value": {
                "Search": "",
                "Sorting": "",
                "countPerPage": {
                    "Page": 1,
                    "ItemPerPage": 100
                }
            }
        }

        response = self.client.post('/apiproyek/wb/User/GetListUserManagement', json=data, headers=headers)
        if response.status_code == 200:
            json_response = response.json()
            print(f"Full Response: {json_response}") 
            # msg = json_response.get('value', {}).get('response')
            # print(f"Message: {msg}")
        else:
            print(f'Create failed: {response.text}')

