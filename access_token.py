import requests

class AccessToken:
    def __init__(self):
        self.token = None

    def fetch_token(self):
        url = 'https://dev-apiv1.1000saudara.com/auth/access'
        headers = {
            'X-MSSAPI-KEY': 'DPEqC6x0Rh8eU5QhtjS1'
        }
        response = requests.post(url, headers=headers, data='')

        if response.status_code == 200:
            self.token = response.json().get('token')
            print(f'Token retrieved: {self.token}')
        else:
            print(f'Failed to retrieve token: {response.text}')
