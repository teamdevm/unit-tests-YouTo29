import requests

class Converter:
    def get_exchange_rate(self, currency: str) -> float:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        data = response.json()
        return float(data['bpi'][currency]['rate_float'])

    def convert_bitcoins(self, currency: str, coins: int) -> float:
        return coins * self.get_exchange_rate(currency)
