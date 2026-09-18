import httpx


with httpx.Client(
    proxy="socks5://127.0.0.1:10808"
) as client:


    response = client.get("https://api.telegram.org")

    print(response.status_code)
    print(response.text)