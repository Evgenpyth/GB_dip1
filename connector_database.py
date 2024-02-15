from sqlalchemy import create_engine,  text

# Замените значения username, password, dbname и port на свои реальные данные
DB_URL = 'postgresql://postgres:26426833@localhost:5432/postgres'

# Создание объекта Engine для подключения к базе данных
engine = create_engine(DB_URL)

# Подключение к базе данных
connection = engine.connect()

# Выполнение SQL запроса
query = text("SELECT * FROM products")
result = connection.execute(query)

# Вывод результата запроса
for row in result:
    print(row)

# Закрытие соединения
connection.close()