from bs4 import BeautifulSoup as bs
import requests
import json
import lxml

URL = 'https://www.mashina.kg/'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
car_list = soup.find('div', class_="category-block cars").find_all('div', class_="category-block-content-item")
cars_item_title = []
cars_item_price = []
cars_item_link = []
cars = []
for car in car_list:
    cars_item_title.append(car.find('div', class_="main-title").text.strip())
    try:
        price_tag = car.find('span', class_="currency-1")
        cars_item_price.append(price_tag.find('strong').text)
    except Exception:
        cars_item_price.append('Договорная')
    cars_item_link.append(car.find('img').get('src'))
count = 1
for a, b, c in zip(cars_item_title,cars_item_price,cars_item_link):
    cars.append({"№":count, "Название":a,"Цена":b,"Фото":c})
    count += 1


car_big_list = soup.find('div', class_="category-block commercial").find_all('div', class_="category-block-content-item")
cars_big_item_title = []
cars_big_item_price = []
cars_big_item_link = []
cars_big = []
for car in car_big_list:
    cars_big_item_title.append(car.find('div', class_="main-title").text.strip())
    try:
        price_tag_3 = car.find('span', class_="currency-1")
        cars_big_item_price.append(price_tag_3.find('strong').text)
    except Exception:
        cars_big_item_price.append('Договорная')
    cars_big_item_link.append(car.find('img').get('src'))
count_big = 1
for a, b, c in zip(cars_big_item_title,cars_big_item_price,cars_big_item_link):
    cars.append({"№":count_big, "Название":a,"Цена":b,"Фото":c})
    count_big += 1


car_big_spec_list = soup.find('div', class_="category-block spec").find_all('div', class_="category-block-content-item")
cars_big_spec_item_title = []
cars_big_spec_item_price = []
cars_big_spec_item_link = []
cars_big_spec = []
for car in car_big_spec_list:
    cars_big_spec_item_title.append(car.find('div', class_="main-title").text.strip())
    try:
        price_tag_4 = car.find('span', class_="currency-1")
        cars_big_spec_item_price.append(price_tag_4.find('strong').text)
    except Exception:
        cars_big_spec_item_price.append('Договорная')
    cars_big_spec_item_link.append(car.find('img').get('src'))
count_big_spec = 1
for a, b, c in zip(cars_big_spec_item_title,cars_big_spec_item_price,cars_big_spec_item_link):
    cars.append({"№":count, "Название":a,"Цена":b,"Фото":c})
    count_big_spec += 1


cars_parts_list = soup.find('div', class_="category-block parts").find_all('div', class_="category-block-content-item")
cars_parts_item_title = []
cars_parts_item_price = []
cars_parts_item_link = []
cars_parts = []
for car in cars_parts_list:
    cars_parts_item_title.append(car.find('div', class_="main-title").text.strip())
    try:
        price_tag_2 = car.find('span', class_="currency-1")
        cars_parts_item_price.append(price_tag_2.find('strong').text)
    except Exception:
        cars_parts_item_price.append('Договорная')
    cars_parts_item_link.append(car.find('img').get('src'))
count_parts = 1
for a, b, c in zip(cars_parts_item_title,cars_parts_item_price,cars_parts_item_link):
    cars.append({"№":count, "Название":a,"Цена":b,"Фото":c})
    count_parts += 1


cars_moto_1_list = soup.find('div', class_="category-block service").find_all('div', class_="category-block-content-item")
cars_moto_1_item_title = []
cars_moto_1_item_price = []
cars_moto_1_item_link = []
cars_moto_1 = []
for car in cars_moto_1_list:
    cars_moto_1_item_title.append(car.find('div', class_="main-title").text.strip())
    try:
        price_tag_5 = car.find('span', class_="currency-1")
        cars_moto_1_item_price.append(price_tag_5.find('strong').text)
    except:
        cars_moto_1_item_price.append('Договорная')
    cars_moto_1_item_link.append(car.find('img').get('src'))
count_moto = 1
for a, b, c in zip(cars_moto_1_item_title,cars_moto_1_item_price,cars_moto_1_item_link):
    cars.append({"№":count, "Название":a,"Цена":b,"Фото":c})
    count_moto += 1


cars_moto_list = soup.find('div', class_="category-block moto").find_all('div', class_="category-block-content-item")
cars_moto_item_title = []
cars_moto_item_price = []
cars_moto_item_link = []
cars_moto = []
for car in cars_moto_list:
    cars_moto_item_title.append(car.find('div', class_="main-title").text.strip())
    try:
        price_tag_6 = car.find('span', class_="currency-1")
        cars_moto_item_price.append(price_tag_6.find('strong').text)
    except:
        cars_moto_item_price.append('Договорная')
    cars_moto_item_link.append(car.find('img').get('src'))
count_moto = 1
for a, b, c in zip(cars_moto_item_title,cars_moto_item_price,cars_moto_item_link):
    cars.append({"№":count, "Название":a,"Цена":b,"Фото":c})
    count_moto += 1


cars_action_list = soup.find('div', class_="category-block buy").find_all('div', class_="category-block-content-item")
cars_action_item_title = []
cars_action_item_price = []
cars_action_item_link = []
cars_action = []
for car in cars_action_list:
    cars_action_item_title.append(car.find('div', class_="main-title").text.strip())
    try:
        price_tag_7 = car.find('span', class_="currency-1")
        cars_action_item_price.append(price_tag_7.find('strong').text)
    except:
        cars_parts_item_price.append('Договорная')
    cars_action_item_link.append(car.find('img').get('src'))
count_action = 1
for a, b, c in zip(cars_action_item_title,cars_action_item_price,cars_action_item_link):
    cars.append({"№":count, "Название":a,"Цена":b,"Фото":c})
    count_action += 1


ress = []
ress.append({"легковые Авто":cars})
ress.append({"Коммерческие Авто":cars_big})
ress.append({"спецтехника":cars_big_spec})
ress.append({"Запчасти":cars_parts})
ress.append({"Услуги":cars_moto_1})
ress.append({"Мото":cars_moto})
ress.append({"Куплю":cars_action})

with open('dp2.json', 'a') as file:
    json.dump(ress,file,ensure_ascii=False,indent=4)