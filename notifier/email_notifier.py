import requests
from bs4 import BeautifulSoup
from config.config import MARKETPLACE_URL

def check_skin_availability(skin_name):
    response = requests.get(MARKETPLACE_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        skins = soup.find_all('div', class_='skin-item')
        for skin in skins:
            if skin_name.lower() in skin.text.lower():
                return True
    return False
