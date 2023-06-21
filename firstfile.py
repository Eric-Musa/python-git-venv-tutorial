import requests, json

website_url = 'https://httpbin.org/get'
portfolio_url = 'https://ericmusa.com'


if __name__ == "__main__":
    response = requests.get(website_url)
    data = response.json()
    # print(json.dumps(data, indent=2))
    print(data)
