import httpx


class Client:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.example.com"

    async def request(self, method: str, path: str, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.request(
                method,
                f"{self.base_url}{path}",
                headers=headers,
                **kwargs
            )

        response.raise_for_status()
        return response.json()