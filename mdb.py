import requests
import time
def get_closest_users(user_id = 9082):
    url = "https://api.mbd.xyz/v1/farcaster/users/feed/similar"

    payload = {
        "user_id": str(user_id),
        "top_k": 25
    }
    headers = {
        "accept": "application/json",
        "HTTP-Referer": "https://docs.mbd.xyz/",
        "X-Title": "mbd_docs",
        "content-type": "application/json",
        "x-api-key": "mbd-API-KEY",
    }

    response = requests.post(url, json=payload, headers=headers)
    
    return response.json()
    