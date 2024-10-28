# from locust import HttpUser, task
# from access_token import AccessToken 

# class LoginTask(HttpUser):
#     token_manager = AccessToken()

#     def on_start(self):
#         # Panggil method untuk mengambil token saat pengguna mulai
#         self.token_manager.fetch_token()

#     @task
#     def login(self):
#         headers = {
#             'Content-Type': 'application/json',
#             'Authorization': f'Bearer {self.token_manager.token}'
#         }
#         data = {
#             "Token": "",
#             "UserCode": "",
#             "Origins": {
#                 "Source": "app_mitra",
#                 "Version": ""
#             },
#             "Value": {
#                 "Username": "088210068283",
#                 "Password": "12345"
#             }
#         }
#         response = self.client.post('/apiproyek/wb/User/Login', json=data, headers=headers)
#         if response.status_code == 200:
#             print("Login successful!")
#         else:
#             print(f'Login failed: {response.text}')

from locust import HttpUser, task
from access_token import AccessToken 
class LoginTask(HttpUser):
    token_manager = AccessToken()
    host = 'https://dev-apiv1.1000saudara.com'

    def on_start(self):
        # Mengambil token saat pengguna mulai
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
        response = self.client.post('/apiproyek/wb/User/Login', json=data, headers=headers)
        if response.status_code == 200:
            print("Login successful!")
        else:
            print(f'Login failed: {response.text}')
