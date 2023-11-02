import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://www.hemkop.se/sok?q=pepparsalami&sort=relevance&page=1"  
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find("h3")
        data = data.get_text()
        return data
    else:
        return None
    

print(scrape_data())