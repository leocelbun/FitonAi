import requests

def fetch_market_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 10, 'page': 1}
    response = requests.get(url, params=params)
    return response.json()

def analyze_data(market_data):
    prices = [coin['current_price'] for coin in market_data]
    average_price = sum(prices) / len(prices)
    return average_price

if __name__ == "__main__":
    data = fetch_market_data()
    average_price = analyze_data(data)
    print(f'Average market price: {average_price}')

