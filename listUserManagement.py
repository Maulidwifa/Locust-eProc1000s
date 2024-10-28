from locust import HttpUser, task, between
from access_token import AccessToken

class   ListUserManajement(HttpUser):
    token_manager = AccessToken()
    wait_time = between(1, 3)
    host = 'https://dev-apiv1.1000saudara.com'

    def on_start(self):
        # Mengambil token saat pengguna mulai
        self.token_manager.fetch_token()

    @task
    def listUser(self):
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