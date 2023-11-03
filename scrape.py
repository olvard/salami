import requests
from bs4 import BeautifulSoup
from datetime import date


def scrape_data():
    url = "https://www.hemkop.se/sok?q=pepparsalami&sort=relevance&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        data = list()
        price = soup.find("h3")
        data.append(price.get_text())
        offer = soup.find('div', class_='sc-c05686a6-5 gqmFdn')
        data.append(offer.get_text())

        return data
    else:
        return None


def get_date():
    today = date.today()
    return today


print(scrape_data())
print(get_date())
