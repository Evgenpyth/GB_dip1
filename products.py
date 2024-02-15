import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

# Создание объекта Engine для подключения к базе данных PostgreSQL
#DB_URL = 'postgresql://postgres:26426833@localhost:5432/postgres'
#engine = create_engine(DB_URL)


# Функция для парсинга названий товаров, их цен и описаний
def parse_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', class_='dtList i-dtList j-card-item')

    for product in products:
        # Парсинг данных о товаре
        product_id = product.get('data-popup-nm-id')
        product_name = product.find('span', class_='goods-name').text.strip()
        category_id = product.get('data-category')
        price = product.find('span', class_='price').text.strip()
        description = product.find('div', class_='goods-description').text.strip()
        brand = product.find('strong', class_='brand-name').text.strip()
        url = product.find('a', class_='ref_goods_n_p')['href']

        # Вывод информации о товаре
        print("Product ID:", product_id)
        print("Product Name:", product_name)
        print("Category ID:", category_id)
        print("Price:", price)
        print("Description:", description)
        print("Brand:", brand)
        print("URL:", url)
        print("\n")


# URL главной страницы Wildberries.ru с товарами
url = 'https://www.wildberries.kz/catalog/muzhchinam/odezhda/bryuki-i-shorty'

# Парсинг названий товаров, их цен и описаний по указанному URL
parse_products(url)
