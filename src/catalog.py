from src.product import *

class Category:
    # Атрибуты класса для хранения общей информации
    total_categories = 0
    total_products = 0

    name: str  # название
    description: str  # описание
    products: list[Product]  # список товаров категории

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
                    raise ValueError(
                        "Все элементы списка продуктов должны быть объектами класса Product"
                    )
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