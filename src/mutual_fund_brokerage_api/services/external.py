import requests

class ExternalService:
    def __init__(self, url: str):
        self.url = url

    def call_api(self, endpoint: str, method: str = 'GET', data: dict = None, headers: dict = None) -> dict:
        if headers is None:
            headers = {}
        if method == 'GET':
            response = requests.get(f"{self.url}/{endpoint}", headers=headers)
        elif method == 'POST':
            response = requests.post(f"{self.url}/{endpoint}", json=data, headers=headers)
        return response.json()
