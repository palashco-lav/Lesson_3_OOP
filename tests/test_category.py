from io import StringIO
from unittest.mock import patch

import pytest

from src.category import Category, CategoryIterator, Order
from src.product import Product


def test_category_init():
    # Создаем тестовые продукты
    product1 = Product("iPhone 14", "Смартфон Apple", 79990.0, 10)
    product2 = Product("Samsung S22", "Смартфон Samsung", 69990.0, 15)

    # Создаем категорию с продуктами
    category = Category(
        name="Смартфоны",
        description="Категория смартфонов",
        products=[product1, product2],
    )

    # Проверяем инициализацию
    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert category.category_product_count == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_category_without_products():
    # Создаем категорию без продуктов
    category = Category(
        name="Планшеты", description="Категория планшетов", products=None
    )

    # Проверяем инициализацию
    assert category.name == "Планшеты"
    assert category.description == "Категория планшетов"
    assert category.category_product_count == 0
    assert Category.total_categories == 2
    assert Category.total_products == 2  # не изменилось, так как нет продуктов


def test_category_count():
    # Создаем несколько категорий
    category1 = Category("Ноутбуки", "Категория ноутбуков", [])
    category2 = Category("Планшеты", "Категория планшетов", [])
    category3 = Category("Смартфоны", "Категория смартфонов", [])

    # Проверяем счетчик категорий
    assert Category.total_categories == 5  # +3 новых категории
    assert category1.category_count == 5
    assert category2.category_count == 5
    assert category3.category_count == 5


def test_product_count():
    # Создаем категорию с продуктами
    product1 = Product("iPhone 14", "Смартфон Apple", 79990.0, 10)
    product2 = Product("Samsung S22", "Смартфон Samsung", 69990.0, 15)
    product3 = Product("Xiaomi 13", "Смартфон Xiaomi", 49990.0, 20)

    category = Category(
        name="Смартфоны",
        description="Категория смартфонов",
        products=[product1, product2, product3],
    )

    # Проверяем счетчик продуктов
    assert Category.total_products == 5  # +3 новых продукта в category
    assert category.product_count == 5


def test_invalid_init():
    # Проверяем валидацию входных данных
    try:
        Category(123, "Описание", [])  # некорректное имя
        assert False, "Должна быть ошибка при неверном типе имени"
    except ValueError:
        pass

    try:
        Category("", "Описание", [])  # пустое имя
        assert False, "Должна быть ошибка при пустом имени"
    except ValueError:
        pass

    try:
        Category("Категория", 123, [])  # некорректное описание
        assert False, "Должна быть ошибка при неверном типе описания"
    except ValueError:
        pass

    try:
        Category("Категория", "", [])  # пустое описание
        assert False, "Должна быть ошибка при пустом описании"
    except ValueError:
        pass

    try:
        Category("Категория", "Описание", "не список")  # некорректный тип продуктов
        assert False, "Должна быть ошибка при неверном типе списка продуктов"
    except ValueError:
        pass


def test_add_product():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию
    category = Category("Электроника", "Электронные устройства", [])

    # Добавляем продукты в категорию
    category.add_product(product1)
    category.add_product(product2)

    # Проверяем, что продукты были добавлены
    assert product1 in category._Category__products
    assert product2 in category._Category__products

    # Проверяем общее количество продуктов в категории
    assert category.category_product_count == 2

    # Проверяем общее количество товаров во всех категориях
    assert Category.total_products == 7


def test_get_product_info():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Проверяем вывод информации о продуктах
    expected_output = (
        "Смартфон, 1000.0 руб. Остаток: 10 шт.\n" "Ноутбук, 5000.0 руб. Остаток: 5 шт."
    )
    with patch("sys.stdout", new=StringIO()) as fake_out:
        print(category.get_product_info)
        assert fake_out.getvalue().strip() == expected_output.strip()


def test_str():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Проверяем вывод информации о категории
    expected_str = "Электроника, количество продуктов: 15"
    assert str(category) == expected_str


def test_category_iterator():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Создаём итератор для категории
    category_iterator = CategoryIterator(category)

    # Проверяем итерацию по товарам
    products = []
    for product in category_iterator:
        products.append(product)

    assert products == [product1, product2]


def test_products_property():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 1000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 5000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    # Проверяем свойство products
    expected_products_info = f"{product1}\n" f"{product2}\n"
    assert category.products == expected_products_info


def test_middle_price():
    # Создаём несколько продуктов
    product1 = Product("Смартфон", "Современный смартфон с большим экраном", 4000.0, 10)
    product2 = Product("Ноутбук", "Мощный ноутбук для работы", 2000.0, 5)

    # Создаём категорию и добавляем продукты
    category = Category("Электроника", "Электронные устройства", [product1, product2])

    assert category.middle_price() == 3000.0


def test_order_creation_with_valid_quantity():
    # Arrange
    product = Product("Ноутбук", "Мощный", 1000.0, 5)

    # Act
    order = Order(product, 2)

    # Assert
    assert order.quantity == 2
    assert product.quantity == 3  # Проверка уменьшения остатка
    assert order.calculate_total() == 2000.0


def test_order_with_negative_quantity_raises_error():
    # Arrange
    product = Product("Телефон", "Стильный", 500.0, 10)

    # Act & Assert
    with pytest.raises(ValueError, match="Некорректное количество товара"):
        Order(product, -1)


def test_update_quantity_changes_total():
    # Arrange
    product = Product("Планшет", "Красненький!", 300.0, 8)
    order = Order(product, 3)

    # Act
    order.update_quantity(4)

    # Assert
    assert order.quantity == 4
    assert order.calculate_total() == 1200.0
    assert product.quantity == 4  # 8 - 3 - (4-3) = 4


def test_invalid_product_raises_attribute_error():
    # Arrange
    class FakeProduct:
        pass

    fake_product = FakeProduct()

    # Act & Assert
    with pytest.raises(AttributeError, match="атрибут 'price'"):
        Order(fake_product, 1)


def test_display_info_formatting():
    # Arrange
    product = Product("Часы", "Как у олигархов", 150.0, 20)
    order = Order(product, 5)

    # Act
    info = order.display_info

    # Assert
    assert "Часы × 5 = 750.00 ₽" in info
