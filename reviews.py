import requests
import BeautifulSoup
import create_engine

# Создание объекта Engine для подключения к базе данных PostgreSQL
DB_URL = 'postgresql://postgres:26426833@localhost:5432/postgres'
engine = create_engine(DB_URL)

# Функция для парсинга отзывов о товарах
def parse_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    reviews = soup.find_all('div', class_='comments-item')

    for review in reviews:
        customer_name = review.find('div', class_='comment-user').text.strip()
        rating = int(review.find('span', class_='rating').text.strip())
        comment = review.find('div', class_='comment-text').text.strip()
        date_posted = review.find('span', class_='comment-date').text.strip()

        # Сохранение данных в базу данных
        with engine.connect() as connection:
            connection.execute(
                "INSERT INTO reviews (customer_name, rating, comment, date_posted) VALUES (%s, %s, %s, %s)",
                (customer_name, rating, comment, date_posted)
            )

# URL страницы с отзывами о товаре на Wildberries.ru
url = 'https://www.wildberries.ru/catalog/1234567/otzyvy'

# Парсинг отзывов о товаре по указанному URL
parse_reviews(url)