import requests


class UsersClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def get_user(self, user_id: int):
        return requests.get(f"{self.BASE_URL}/users/{user_id}", timeout=self.timeout)

    def create_user(self, payload: dict):
        return requests.post(f"{self.BASE_URL}/users", json=payload, timeout=self.timeout)
