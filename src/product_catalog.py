import json

class Product:
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        # Валидация имени
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        self.name = name

        # Валидация описания
        if not isinstance(description, str) or not description:
            raise ValueError("Описание должно быть непустой строкой")
        self.description = description

        # Валидация цены
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = float(price)

        # Валидация количества
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть положительным целым числом")
        self.quantity = quantity


class Category:
    # Атрибуты класса для хранения общей информации
    total_categories = 0
    total_products = 0

    name: str               # название
    description: str        # описание
    products: list[Product] # список товаров категории

    def __init__(self, name, description, products):
        # Валидация имени категории
        if not isinstance(name, str) or not name:
            raise ValueError("Название категории должно быть непустой строкой")
        self.name = name

        # Валидация описания категории
        if not isinstance(description, str) or not description:
            raise ValueError("Описание категории должно быть непустой строкой")
        self.description = description

        # Валидация списка продуктов
        if products:
            if not isinstance(products, list):
                raise ValueError("Список продуктов должен быть типа list")
            for product in products:
                if not isinstance(product, Product):
                    raise ValueError("Все элементы списка продуктов должны быть объектами класса Product")
        self.products = products if products else []

        # При создании нового объекта увеличиваем счетчики
        Category.total_categories += 1
        Category.total_products += len(self.products)

    @property
    def category_count(self):
        return self.total_categories

    @property
    def product_count(self):
        return self.total_products

def load_data_from_json(file_path) -> list[dict]:
    """
        Функция для загрузки данных из JSON файла и создания объектов классов Category и Product.

        Параметры:
        file_path (str): путь к JSON файлу с данными.

        Возвращает:
        list[Category]: список объектов класса Category, созданных на основе данных из файла.
        """
    categories = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for category_data in data:
        name = category_data['name']
        description = category_data['description']
        products = [
            Product(
                product_data['name'],
                product_data['description'],
                product_data['price'],
                product_data['quantity']
            )
            for product_data in category_data['products']
        ]
        category = Category(name, description, products)
        categories.append(category.name)

    return categories

