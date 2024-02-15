import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_products(url):
    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-контента страницы
        soup = BeautifulSoup(response.content, 'html.parser')

        # Создаем списки для хранения данных о товарах
        product_ids = []
        product_names = []
        category_ids = []
        prices = []
        descriptions = []
        brands = []
        urls = []

        # Находим все блоки с информацией о товарах
        products = soup.find_all('div', class_='dtList i-dtList j-card-item')

        # Проходимся по каждому блоку с товаром
        for product in products:
            # Парсим данные о товаре и добавляем их в соответствующие списки
            product_ids.append(product.get('data-popup-nm-id'))
            product_names.append(product.find('span', class_='goods-name').text.strip())
            category_ids.append(product.get('data-category'))
            prices.append(product.find('span', class_='price').text.strip())
            descriptions.append(product.find('div', class_='goods-description').text.strip())
            brands.append(product.find('strong', class_='brand-name').text.strip())
            urls.append('https://sklad.kz/' + product.find('a', class_='ref_goods_n_p')['href'])

        # Создаем DataFrame из данных о товарах
        df = pd.DataFrame({
            'product_id': product_ids,
            'product_name': product_names,
            'category_id': category_ids,
            'price': prices,
            'description': descriptions,
            'brand': brands,
            'url': urls
        })

        # Выводим первые строки DataFrame в консоль
        print(df.head())

        # Сохраняем DataFrame в Excel-файл
        df.to_excel('wildberries_products.xlsx', index=False)

    else:
        print('Ошибка при загрузке страницы:', response.status_code)

# URL страницы с товарами на Wildberries
url = 'https://www.wildberries.ru/catalog/66783447/detail.aspx'

# Вызываем функцию для парсинга товаров по указанному URL
parse_products(url)
