from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
telephone_list = soup.find_all('div', class_='item product_listbox oh')
telephony = []
for phone in telephone_list:
    title = phone.find('div', class_="listbox_title oh").find('strong').text
    price = phone.find('div', class_="listbox_price text-center").find('strong').text
    link = 'https://www.kivano.kg' + phone.find('img').get('src')
    telephony.append({
        "Название":title,
        "Цена":price,
        "Фотография":link
    })

with open('dp1.json', 'a') as file:
    json.dump(telephony,file, ensure_ascii=False, indent=4)