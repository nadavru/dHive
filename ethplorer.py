import requests

def get_wallet_info(address):
    API_KEY = 'API-KEY'
    # url = f'https://api.ethplorer.io//getLastBlock?apiKey={API_KEY}'
    # url = f'https://api.ethplorer.io//getAddressInfo/{address}?apiKey={API_KEY}'
    url = f'https://api.ethplorer.io//getAddressHistory/{address}?apiKey={API_KEY}'
    # url = f'https://api.ethplorer.io/getAddressInfo/{address}?apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

def get_value(value, decimals):
    return int(value) / 10 ** int(decimals)

def parse_wallet(data):
        
    len(data["operations"])
    user = []
    for operation in data["operations"]:
        dict = {}
        dict['timestamp'] = operation['timestamp']
        dict['value'] = get_value(operation['value'], operation['tokenInfo']['decimals'])
        dict['symbol'] = operation['tokenInfo']['symbol']
        dict['name'] = operation['tokenInfo']['publicTags']
        user.append(dict)
    return user

def get_wallet_data(address):
    data = get_wallet_info(address)
    return parse_wallet(data)