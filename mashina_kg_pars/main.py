from bs4 import BeautifulSoup as bs
import requests
import json
import lxml

URL = 'https://www.mashina.kg/'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
car_list = soup.find_all('div', class_="main-image")
car_json_list = []
for car in car_list:
    title = car.find('div', class_="main-title").text.strip()
    price_tag = car.find('span', class_="currency-1")
    if price_tag:
        price = price_tag.find('strong').text
    link = car.find('img').get('src')
    # print(f'Название - {title}\nЦена - {price}\nСсылка - {link}\n\n')
    car_json_list.append({
        "Название":title,
        "Цена":price,
        "Ссылка к фото":link
    })
with open('dp2.json', 'a') as file:
    json.dump(car_json_list,file,ensure_ascii=False,indent=4)





















#     telephony.append({
#         "Название":title,
#         "Цена":price,
#         "Фотография":link
#     })

# with open('dp1.json', 'a') as file:
#     json.dump(telephony,file, ensure_ascii=False, indent=4)