import requests
import time

def get_wallet_from_userid(user_id):
    
    url = f"https://build.far.quest/farcaster/v2/user?fid={user_id}"

    headers = {
        "accept": "application/json",
        "API-KEY": "API-KEY",
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 429:
        print("sleeping")
        time.sleep(1.5)
        response = requests.get(url, headers=headers)
    try:
        data = response.json()
        return data['result']['user']['allConnectedAddresses']['ethereum']
    except:
        print("error")
        print(response)
        print(response.text)
        return None
