import json

from src.catalog import *

def load_data_from_json(file_path) -> list[str]:
    """
    Функция для загрузки данных из JSON файла и создания объектов классов Category и Product.

    Параметры:
    file_path (str): путь к JSON файлу с данными.

    Возвращает:
    list[Category]: список объектов класса Category, созданных на основе данных из файла.
    """
    categories = []
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for category_data in data:
        name = category_data["name"]
        description = category_data["description"]
        products = [
            Product(
                product_data["name"],
                product_data["description"],
                product_data["price"],
                product_data["quantity"],
            )
            for product_data in category_data["products"]
        ]
        category = Category(name, description, products)
        categories.append(category.name)

    return categories